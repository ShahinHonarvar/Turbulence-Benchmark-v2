def if_contains_anagrams(strings):

    def is_anagram(str1, str2):
        return len(str1) >= 3 and len(str2) >= 3 and (sorted(str1) == sorted(str2))

    def normalize(str):
        return str.lower()
    strings = [normalize(s) for s in strings]
    anagram_pairs = 0
    n = len(strings)
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                anagram_pairs += 1
                if anagram_pairs >= 5:
                    return True
    return False