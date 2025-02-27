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
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count <= 255