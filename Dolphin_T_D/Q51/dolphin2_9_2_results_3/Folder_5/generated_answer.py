from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for word in lst:
        if len(word) >= 3:
            c = Counter(word.lower())
            for j in range(len(lst)):
                if lst[j] != word:
                    if Counter(lst[j].lower()) == c:
                        count += 1
    if count >= 4:
        return True
    else:
        return False