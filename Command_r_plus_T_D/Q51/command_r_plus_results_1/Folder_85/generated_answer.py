def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized not in anagram_dict:
            anagram_dict[normalized] = []
        anagram_dict[normalized].append(word)
    anagram_pairs = sum((1 for words in anagram_dict.values() if len(words) > 1))
    return anagram_pairs <= 276