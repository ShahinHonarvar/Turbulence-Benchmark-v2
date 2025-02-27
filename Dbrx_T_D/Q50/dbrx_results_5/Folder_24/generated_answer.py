from collections import defaultdict

def if_contains_anagrams(lst):
    anagrams = defaultdict(int)
    for word in lst:
        sorted_word = ''.join(sorted(word.lower()))
        anagrams[sorted_word] += 1
        if anagrams[sorted_word] == 65:
            return True
    return False