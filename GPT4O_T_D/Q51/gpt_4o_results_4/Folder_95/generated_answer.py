def if_contains_anagrams(words):

    def normalize(word):
        return ''.join(sorted(word.lower()))
    anagram_groups = {}
    for word in words:
        if len(word) >= 3:
            key = normalize(word)
            if key in anagram_groups:
                anagram_groups[key] += 1
            else:
                anagram_groups[key] = 1
    anagram_pairs = 0
    for count in anagram_groups.values():
        anagram_pairs += count * (count - 1) // 2
    return anagram_pairs <= 6