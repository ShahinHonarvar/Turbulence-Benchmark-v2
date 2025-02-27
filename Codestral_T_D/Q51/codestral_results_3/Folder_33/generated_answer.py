from collections import Counter

def if_contains_anagrams(strings):
    count = 0
    anagrams = {}
    for string in strings:
        lower_string = string.lower()
        if len(lower_string) >= 3:
            sorted_string = ''.join(sorted(lower_string))
            if sorted_string in anagrams:
                anagrams[sorted_string].append(string)
            else:
                anagrams[sorted_string] = [string]
    for key in anagrams:
        length = len(anagrams[key])
        count += length * (length - 1) // 2
    return count <= 85