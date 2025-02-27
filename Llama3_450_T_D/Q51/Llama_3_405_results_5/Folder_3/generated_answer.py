def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s = ''.join((e for e in s if e.isalpha())).lower()
        if len(s) < 3:
            continue
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            count += anagrams[sorted_s]
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    return count <= 66