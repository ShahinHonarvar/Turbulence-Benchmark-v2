def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        key = ''.join(sorted(lower_string))
        if key in anagrams:
            anagrams[key].append(lower_string)
        else:
            anagrams[key] = [lower_string]
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count <= 257