def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            anagrams.setdefault(sorted_string, []).append(string)
    for k, v in anagrams.items():
        count += len(v) * (len(v) - 1) // 2
    return count <= 206