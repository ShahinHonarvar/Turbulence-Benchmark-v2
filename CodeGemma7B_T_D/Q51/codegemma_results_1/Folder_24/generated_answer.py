from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        key = ''.join(sorted([ch for ch in word.lower() if ch.isalpha() and len(ch) >= 3]))
        anagrams[key].append(word)
    return len(anagrams) <= 96