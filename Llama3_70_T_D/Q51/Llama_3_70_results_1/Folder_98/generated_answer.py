def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string.lower()))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
    for strings in anagrams.values():
        if len(strings) > 1:
            count += len(strings) * (len(strings) - 1) // 2
    return count <= 46