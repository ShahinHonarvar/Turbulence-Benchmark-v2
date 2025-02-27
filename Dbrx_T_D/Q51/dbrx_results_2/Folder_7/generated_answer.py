import itertools

def if_contains_anagrams(string_list):
    anagrams = {}
    count = 0
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    for value in anagrams.values():
        count += len(value) * (len(value) - 1) // 2
    return count <= 445