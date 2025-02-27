from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(set)
    for word in str_list:
        letters = ''.join(sorted(word.lower()))
        if len(letters) >= 3:
            anagrams[letters].add(word)
    return len(anagrams) <= 70