def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        sorted_string = ''.join(sorted(filter(str.isalpha, string.lower())))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    pairs = sum((count * (count - 1) // 2 for count in anagrams.values()))
    return pairs <= 210