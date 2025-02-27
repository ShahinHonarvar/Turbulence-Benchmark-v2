def if_contains_anagrams(lst):
    anagrams = {}
    total_anagrams = 0
    for string in lst:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    for count in anagrams.values():
        total_anagrams += count * (count - 1) // 2
    return total_anagrams <= 74