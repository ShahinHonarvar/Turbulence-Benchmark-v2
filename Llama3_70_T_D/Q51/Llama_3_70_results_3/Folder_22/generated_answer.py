def if_contains_anagrams(lst):
    anagrams = {}
    pairs = 0
    for string in lst:
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted((c for c in string.lower() if c.isalpha())))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 14