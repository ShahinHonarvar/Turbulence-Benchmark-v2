def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for s in strings:
        s = ''.join(filter(str.isalpha, s)).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
            count += anagrams[sorted_s]
        else:
            anagrams[sorted_s] = 1
    return count <= 66 * (len(strings) - 1) // 2