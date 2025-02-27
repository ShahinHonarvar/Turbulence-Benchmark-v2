def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        if len(string) < 3:
            continue
        string = ''.join(filter(str.isalpha, string)).lower()
        sorted_str = ''.join(sorted(string))
        if sorted_str in anagrams:
            anagrams[sorted_str].append(string)
        else:
            anagrams[sorted_str] = [string]
    for key, value in anagrams.items():
        count += len(value) * (len(value) - 1) // 2
    return count <= 64