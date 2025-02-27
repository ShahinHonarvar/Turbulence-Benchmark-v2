def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_count = 0
    anagram_map = {}
    for word in words:
        if len(word) < 3:
            continue
        normalized = normalize(word)
        if normalized in anagram_map:
            anagram_count += 1
            anagram_map[normalized] += 1
        else:
            anagram_map[normalized] = 1
    return anagram_count <= 41