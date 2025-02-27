def if_contains_anagrams(lst):

    def normalize_text(text):
        return ''.join(sorted(text.lower()))
    anagram_dict = {}
    for word in lst:
        normalized = normalize_text(word)
        if len(word) >= 3:
            if normalized in anagram_dict:
                anagram_dict[normalized] += 1
            else:
                anagram_dict[normalized] = 1
    anagram_pairs = sum((1 for count in anagram_dict.values() if count > 1))
    return anagram_pairs <= 24