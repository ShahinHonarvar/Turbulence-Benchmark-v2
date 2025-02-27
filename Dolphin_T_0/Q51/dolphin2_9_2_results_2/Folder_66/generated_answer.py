from collections import Counter

def if_contains_anagrams(lst):
    anagram_pairs = 0
    list_length = len(lst)
    for i in range(list_length):
        if len(lst[i]) >= 3:
            for j in range(i + 1, list_length):
                if len(lst[j]) >= 3 and Counter(lst[i].lower()) == Counter(lst[j].lower()):
                    anagram_pairs += 1
                    if anagram_pairs > 64:
                        return False
    if anagram_pairs <= 64:
        return True
    return False