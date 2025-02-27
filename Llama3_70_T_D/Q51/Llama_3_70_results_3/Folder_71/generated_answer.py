def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    count = sum((1 for v in anagrams.values() if len(v) > 1))
    return count <= 9