def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    for strings in anagrams.values():
        if len(strings) > 1:
            count += len(strings) * (len(strings) - 1) // 2
    return count >= 209