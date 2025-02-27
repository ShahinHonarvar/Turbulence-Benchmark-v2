def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        s = ''.join(filter(str.isalpha, string)).lower()
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s))
            if sorted_str in anagrams:
                anagrams[sorted_str] += 1
            else:
                anagrams[sorted_str] = 1
    for k, v in anagrams.items():
        if v > 1:
            count += v * (v - 1) // 2
    return count <= 65