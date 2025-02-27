def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        lower = string.lower()
        alpha = ''.join(filter(str.isalpha, lower))
        if len(alpha) < 3:
            continue
        sorted_str = ''.join(sorted(alpha))
        if sorted_str in anagrams:
            anagrams[sorted_str] += 1
        else:
            anagrams[sorted_str] = 1
    for k in anagrams:
        count += anagrams[k] * (anagrams[k] - 1) // 2
    return count <= 474