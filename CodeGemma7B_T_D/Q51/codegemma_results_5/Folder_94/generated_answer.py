from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted((w.lower() for w in word if w.isalpha())))
        anagrams[key].append(word)
    return len(anagrams) <= 181