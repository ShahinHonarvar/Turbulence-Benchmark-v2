def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    for k, v in anagrams.items():
        count += len(v) * (len(v) - 1) // 2
    return count <= 25