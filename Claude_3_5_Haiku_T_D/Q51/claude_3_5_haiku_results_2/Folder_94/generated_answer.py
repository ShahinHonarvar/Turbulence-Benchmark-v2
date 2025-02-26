def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def is_valid_anagram(s1, s2):
        return len(s1) >= 3 and len(s1) == len(s2) and is_anagram(s1, s2)
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_valid_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs > 181:
                    return False
    return True