def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(lower_string)
        else:
            anagrams[sorted_string] = [lower_string]
    for k, v in anagrams.items():
        count += len(v) * (len(v) - 1) // 2
    return count >= 98