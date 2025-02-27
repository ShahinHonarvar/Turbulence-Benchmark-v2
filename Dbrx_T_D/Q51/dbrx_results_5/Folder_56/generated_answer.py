from collections import defaultdict

def if_contains_anagrams(string_list):
    anagrams = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted((char.lower() for char in string if char.isalpha())))
        if len(sorted_string) >= 3:
            anagrams[sorted_string].append(string)
    count = sum((1 for group in anagrams.values() if len(group) > 1))
    return count <= 11