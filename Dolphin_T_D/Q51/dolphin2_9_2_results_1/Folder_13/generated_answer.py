from collections import Counter

def if_contains_anagrams(lst):
    n = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            sorted_word = ''.join(sorted(lst[i].lower()))
            for j in range(i + 1, len(lst)):
                if sorted_word == ''.join(sorted(lst[j].lower())):
                    n += 1
    return n <= 54