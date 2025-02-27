def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_low = s.lower()
        if len(s_low) < 3:
            continue
        s_sorted = ''.join(sorted(s_low))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    count = 0
    for k in anagrams:
        count += anagrams[k] * (anagrams[k] - 1) // 2
    return count >= 64