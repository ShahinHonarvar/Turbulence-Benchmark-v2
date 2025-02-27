def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(filter(str.isalpha, string.lower())))
            if sorted_string in anagrams:
                anagrams[sorted_string] += 1
            else:
                anagrams[sorted_string] = 1
    for value in anagrams.values():
        count += value * (value - 1) // 2
    return count <= 29