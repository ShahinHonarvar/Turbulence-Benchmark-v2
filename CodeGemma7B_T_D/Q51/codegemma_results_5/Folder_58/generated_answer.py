from collections import defaultdict

def if_contains_anagrams(str_list):
    anagrams = defaultdict(set)
    for word in str_list:
        key = ''.join(sorted(word.lower()))
        if len(key) < 3:
            continue
        if key in anagrams:
            if len(anagrams[key]) >= 60:
                return False
            anagrams[key].add(word)
        else:
            anagrams[key].add(word)
    return True