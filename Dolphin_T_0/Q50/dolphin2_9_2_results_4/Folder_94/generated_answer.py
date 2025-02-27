from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            for i in range(len(lst)):
                if lst[i] != word and sorted(word.lower()) == sorted(lst[i].lower()):
                    count += 1
    return count >= 46