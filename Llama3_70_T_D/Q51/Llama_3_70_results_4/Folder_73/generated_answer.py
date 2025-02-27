def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) >= 3:
            sorted_str = ''.join(sorted(string))
            if sorted_str in anagrams:
                anagrams[sorted_str].append(string)
            else:
                anagrams[sorted_str] = [string]
    for key in anagrams:
        n = len(anagrams[key])
        count += n * (n - 1) // 2
    return count <= 279