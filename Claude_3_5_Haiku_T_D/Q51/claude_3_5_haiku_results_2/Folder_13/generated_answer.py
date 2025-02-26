def if_contains_anagrams(lst):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())

    def valid_anagram(s1, s2):
        return len(s1) >= 3 and len(s2) >= 3 and is_anagram(s1, s2)
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if valid_anagram(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 54:
                    return False
    return True