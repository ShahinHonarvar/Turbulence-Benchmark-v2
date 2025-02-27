from collections import Counter

def if_contains_anagrams(lst):
    num_anagrams = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            if_anagrams = False
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    if_anagrams = True
                    num_anagrams += 1
                    break
            if if_anagrams:
                break
    return num_anagrams <= 35