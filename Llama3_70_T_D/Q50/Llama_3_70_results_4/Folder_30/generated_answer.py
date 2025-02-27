def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) < 3:
            continue
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for value in anagrams.values():
        if len(value) > 1:
            count += len(value) * (len(value) - 1) // 2
    return count >= 78