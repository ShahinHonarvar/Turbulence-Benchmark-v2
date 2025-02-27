import itertools

def if_contains_anagrams(strings_list):
    anagrams = {}
    for string in strings_list:
        if len(string) >= 3:
            sorted_string = ''.join(sorted(string.lower()))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    pairs_count = sum([len(value) * (len(value) - 1) // 2 for value in anagrams.values()])
    return pairs_count >= 25