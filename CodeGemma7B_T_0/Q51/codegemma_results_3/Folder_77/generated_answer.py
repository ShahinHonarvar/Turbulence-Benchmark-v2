def if_contains_anagrams(str_list):
    anagrams = {}
    for string in str_list:
        key = ''.join(sorted(string.lower()))
        if key in anagrams:
            anagrams[key] += 1
        else:
            anagrams[key] = 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs <= 17