def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s.isalpha():
            if s in anagrams:
                count += 1
                if count > 20:
                    return False
            else:
                anagrams[s] = 1
    return True