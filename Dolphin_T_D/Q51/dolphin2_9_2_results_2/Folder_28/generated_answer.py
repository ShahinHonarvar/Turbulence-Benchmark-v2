def if_contains_anagrams(strings):
    count = 0
    pairs = {}
    for s in strings:
        if len(s) < 3:
            continue
        s_low = s.lower()
        s_sort = ''.join(sorted(s_low))
        if s_sort in pairs:
            pairs[s_sort] += 1
            count += 1
        else:
            pairs[s_sort] = 1
    return count <= 78