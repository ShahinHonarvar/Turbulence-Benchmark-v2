def if_contains_anagrams(lst):
    anagrams = {}
    for string in lst:
        sorted_string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    count = sum((1 for value in anagrams.values() if len(value) > 1))
    return count >= 49