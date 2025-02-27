def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(string)
        else:
            anagrams[sorted_str] = [string]
    pairs = 0
    for value in anagrams.values():
        pairs += len(value) * (len(value) - 1) // 2
    return pairs <= 61