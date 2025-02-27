from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        word = ''.join(sorted(word.lower()))
        if len(word) >= 3:
            count[word] += 1
            if count[word] > 2:
                return False
    return True