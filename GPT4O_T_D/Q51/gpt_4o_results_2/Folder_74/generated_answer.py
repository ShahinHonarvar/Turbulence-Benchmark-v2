def if_contains_anagrams(strings):
    strings = [s.lower() for s in strings]
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string))
        if sorted_str in anagrams:
            count += anagrams[sorted_str]
            if count > 57:
                return False
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    return True