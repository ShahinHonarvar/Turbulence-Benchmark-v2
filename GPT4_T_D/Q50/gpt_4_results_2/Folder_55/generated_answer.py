from collections import defaultdict

def if_contains_anagrams(str_list):
    words = defaultdict(list)
    for word in str_list:
        if len(word) >= 3:
            words[''.join(sorted(word.lower()))].append(word)
    pairs = sum((len(word_list) - 1 for word_list in words.values()))
    return pairs >= 15