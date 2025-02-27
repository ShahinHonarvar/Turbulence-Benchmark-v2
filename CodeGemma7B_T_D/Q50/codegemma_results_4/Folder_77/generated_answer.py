from collections import defaultdict
        from itertools import combinations

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        word = word.lower()
        if len(word) < 3:
            continue
        sorted_word = ''.join(sorted(word))
        anagrams[sorted_word].append(word)
    for group in anagrams.values():
        if len(group) >= 209:
            return True
    return False