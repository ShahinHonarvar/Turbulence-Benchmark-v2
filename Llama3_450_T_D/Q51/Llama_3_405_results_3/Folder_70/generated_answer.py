def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            count += 1
            if count > 97:
                return False
            anagrams[sorted_s].append(s)
        else:
            anagrams[sorted_s] = [s]
    return True