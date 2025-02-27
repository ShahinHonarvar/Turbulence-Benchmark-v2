from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word_pair in zip(lst, lst[1:]):
        w1, w2 = word_pair
        if len(w1) >= 3 and len(w2) >= 3 and (Counter(w1.lower()) == Counter(w2.lower())):
            count += 1
    return count >= 91