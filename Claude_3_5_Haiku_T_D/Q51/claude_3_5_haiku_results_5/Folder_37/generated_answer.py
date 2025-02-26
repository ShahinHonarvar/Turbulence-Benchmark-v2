def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return len(s1) == len(s2) and sorted(s1.lower()) == sorted(s2.lower())

    def count_anagram_pairs(strings):
        n = len(strings)
        pairs = 0
        for i in range(n):
            for j in range(i + 1, n):
                if len(strings[i]) >= 3 and len(strings[j]) >= 3 and is_anagram(strings[i], strings[j]):
                    pairs += 1
        return pairs
    return count_anagram_pairs(strings) <= 206