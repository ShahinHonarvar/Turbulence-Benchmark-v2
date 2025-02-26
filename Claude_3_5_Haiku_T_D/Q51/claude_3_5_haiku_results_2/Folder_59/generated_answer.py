def if_contains_anagrams(string_list):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def count_anagram_pairs(strings):
        pairs = 0
        n = len(strings)
        for i in range(n):
            for j in range(i + 1, n):
                s1, s2 = (strings[i], strings[j])
                if len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2):
                    pairs += 1
        return pairs
    return count_anagram_pairs(string_list) <= 15