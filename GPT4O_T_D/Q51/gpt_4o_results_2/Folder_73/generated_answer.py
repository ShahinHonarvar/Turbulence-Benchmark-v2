def if_contains_anagrams(strings):

    def is_anagram(s1, s2):
        return sorted(s1.lower()) == sorted(s2.lower())
    strings = [s for s in strings if len(s) >= 3]
    n = len(strings)
    anagram_count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if is_anagram(strings[i], strings[j]):
                anagram_count += 1
                if anagram_count > 279:
                    return False
    return True