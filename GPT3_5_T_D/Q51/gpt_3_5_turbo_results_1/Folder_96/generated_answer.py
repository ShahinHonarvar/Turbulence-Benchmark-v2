from collections import Counter

def if_contains_anagrams(strings):
    anagrams = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                anagrams += 1
            if anagrams > 2:
                return False
    return True