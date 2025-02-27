import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string not in anagrams:
                anagrams[sorted_string] = [string]
            else:
                anagrams[sorted_string].append(string)
    count = 0
    for value in anagrams.values():
        if len(value) >= 2:
            count += len(value) * (len(value) - 1) // 2
    return count >= 88