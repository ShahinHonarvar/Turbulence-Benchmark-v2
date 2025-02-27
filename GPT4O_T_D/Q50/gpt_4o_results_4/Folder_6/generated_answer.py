def if_contains_anagrams(words):

    def sorted_str(s):
        return ''.join(sorted(s.lower()))
    anagram_count = 0
    anagram_pairs = set()
    for i in range(len(words)):
        for j in range(i + 1, len(words)):
            if len(words[i]) >= 3 and len(words[j]) >= 3:
                if sorted_str(words[i]) == sorted_str(words[j]):
                    anagram_pairs.add((min(i, j), max(i, j)))
    return len(anagram_pairs) >= 26