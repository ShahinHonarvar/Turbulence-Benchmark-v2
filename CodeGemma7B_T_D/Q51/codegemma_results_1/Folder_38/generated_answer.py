from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        word = ''.join(sorted([char for char in word.lower() if char.isalpha() and len(char) >= 3]))
        anagrams[word].append(word)
    return len(anagrams) <= 416