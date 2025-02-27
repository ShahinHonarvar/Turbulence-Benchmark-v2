def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        lower_string = string.lower()
        if len(lower_string) < 3:
            continue
        sorted_string = ''.join(sorted(lower_string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    count_anagrams = 0
    for key, value in anagrams.items():
        count_anagrams += value * (value - 1) // 2
    return count_anagrams <= 26