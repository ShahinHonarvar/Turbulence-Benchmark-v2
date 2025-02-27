def if_contains_anagrams(strings):
    anagrams_count = 0
    strings = [s.casefold() for s in strings]
    for s1 in strings:
        for s2 in strings:
            if s1 != s2 and sorted(s1) == sorted(s2) and (len(s1) >= 3) and s1.isalpha():
                anagrams_count += 1
                if anagrams_count > 35:
                    return False
    return True