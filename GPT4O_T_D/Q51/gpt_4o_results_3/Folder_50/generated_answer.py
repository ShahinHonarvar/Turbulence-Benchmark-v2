def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_dict = {}
    for word in words:
        if len(word) >= 3:
            normalized = normalize(word)
            anagram_dict[normalized] = anagram_dict.get(normalized, 0) + 1
    anagram_pairs = 0
    for count in anagram_dict.values():
        if count > 1:
            anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 47