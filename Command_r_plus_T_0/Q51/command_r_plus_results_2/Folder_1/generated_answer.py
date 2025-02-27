def if_contains_anagrams(lst):

    def normalize_string(s):
        return ''.join(sorted(s.lower()))
    anagram_dict = {}
    for word in lst:
        normalized = normalize_string(word)
        if len(word) >= 3:
            if normalized in anagram_dict:
                anagram_dict[normalized].append(word)
            else:
                anagram_dict[normalized] = [word]
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 30