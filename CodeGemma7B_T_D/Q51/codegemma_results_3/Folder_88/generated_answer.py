from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        char_list = sorted([char.lower() for char in word if char.isalpha()])
        anagrams[tuple(char_list)].append(word)
    return len(anagrams) <= 407