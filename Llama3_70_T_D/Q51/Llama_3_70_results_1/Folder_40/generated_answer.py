def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            count += anagrams[sorted_string]
            anagrams[sorted_string] += 1
        else:
            anagrams[sorted_string] = 1
    return count <= 29