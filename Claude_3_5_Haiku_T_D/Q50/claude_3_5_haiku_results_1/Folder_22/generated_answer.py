def if_contains_anagrams(strings):

    def are_anagrams(s1, s2):
        return len(s1) == len(s2) and len(s1) >= 3 and (sorted(s1.lower()) == sorted(s2.lower()))
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if are_anagrams(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs >= 72