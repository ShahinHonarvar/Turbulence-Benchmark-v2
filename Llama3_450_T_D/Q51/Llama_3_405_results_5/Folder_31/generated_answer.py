def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s_lower))
        if len(sorted_s) >= 3:
            if sorted_s in anagrams:
                anagrams[sorted_s].append(s)
            else:
                anagrams[sorted_s] = [s]
    for values in anagrams.values():
        count += len(values) * (len(values) - 1) // 2
        if count > 65:
            return False
    return True