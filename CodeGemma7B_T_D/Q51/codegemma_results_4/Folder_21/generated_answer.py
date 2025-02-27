from collections import defaultdict

def if_contains_anagrams(strings):
    anagrams = defaultdict(list)
    for string in strings:
        char_list = sorted([char for char in string if char.isalpha() and len(char) >= 3])
        if char_list:
            anagrams[''.join(char_list)].append(string)
    return len(anagrams) <= 26