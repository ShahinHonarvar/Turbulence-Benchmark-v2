from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3 and word.islower():
            c = Counter(word)
            for j in range(len(lst)):
                if lst[j] != word and len(lst[j]) >= 3 and lst[j].islower():
                    if Counter(lst[j]) == c:
                        count += 1
    if count > 58:
        return True
    else:
        return False