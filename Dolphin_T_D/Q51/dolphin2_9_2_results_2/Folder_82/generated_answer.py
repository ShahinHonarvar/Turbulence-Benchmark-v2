from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            for i in range(len(lst)):
                if i != count:
                    if Counter(lst[i].lower()) == c:
                        count += 1
    return count <= 40