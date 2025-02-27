from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(list)
    for word in str_list:
        letters = sorted([c for c in word.lower() if c.isalpha()])
        key = ''.join(letters)
        if len(letters) >= 3:
            anagrams[key].append(word)
    return len(anagrams) <= 89