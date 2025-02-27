import itertools

def if_contains_anagrams(strings):
    anagrams = {}
    count = 0
    for string in strings:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            anagrams[sorted_string] = [string] if sorted_string not in anagrams else anagrams[sorted_string] + [string]
    for value in anagrams.values():
        if len(value) >= 2:
            count += len(value) * (len(value) - 1) // 2
    return count >= 70