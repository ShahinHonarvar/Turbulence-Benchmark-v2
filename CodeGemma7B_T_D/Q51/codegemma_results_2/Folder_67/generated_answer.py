from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            anagrams[word].append(word)
    return len(list(filter(lambda x: len(x) > 1, anagrams.values()))) <= 5