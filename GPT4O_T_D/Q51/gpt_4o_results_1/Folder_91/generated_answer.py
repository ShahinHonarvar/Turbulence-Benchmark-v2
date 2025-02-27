def if_contains_anagrams(lst):

    def are_anagrams(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    anagram_pairs = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and are_anagrams(lst[i], lst[j]):
                anagram_pairs += 1
                if anagram_pairs > 88:
                    return False
    return True