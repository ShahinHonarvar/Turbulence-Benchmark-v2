def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        string = ''.join(filter(str.isalpha, string)).lower()
        if len(string) < 3:
            continue
        sorted_string = ''.join(sorted(string))
        if sorted_string in anagrams:
            anagrams[sorted_string].append(string)
        else:
            anagrams[sorted_string] = [string]
    pairs = sum((len(value) * (len(value) - 1) // 2 for value in anagrams.values()))
    return pairs <= 70