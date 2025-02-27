def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) < 3:
            continue
        sorted_str = ''.join(sorted(string.lower()))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(string)
        else:
            anagrams[sorted_str] = [string]
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count >= 58