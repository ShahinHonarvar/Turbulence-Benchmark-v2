def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) >= 3:
            s_sorted = ''.join(sorted(s))
            if s_sorted in anagrams:
                anagrams[s_sorted] += 1
            else:
                anagrams[s_sorted] = 1
    for k in anagrams:
        count += anagrams[k] * (anagrams[k] - 1) // 2
    return count <= 78