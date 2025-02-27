def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string = string.lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for value in anagrams.values():
        n = len(value)
        count += n * (n - 1) // 2
    return count <= 85