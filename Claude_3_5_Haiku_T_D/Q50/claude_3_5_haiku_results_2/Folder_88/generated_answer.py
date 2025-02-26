def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) == len(str2) and len(str1) >= 3 and (sorted(str1.lower()) == sorted(str2.lower()))
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
    return anagram_pairs >= 34