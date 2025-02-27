import collections
import string

def if_contains_anagrams(lst):
    pair_count = 0
    english_letters = string.ascii_lowercase
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            anagrams = set(lst[i].lower()).intersection(set(english_letters))
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3:
                    if set(lst[j].lower()).intersection(set(english_letters)) == anagrams:
                        pair_count += 1
                        if pair_count > 366:
                            return False
    return true