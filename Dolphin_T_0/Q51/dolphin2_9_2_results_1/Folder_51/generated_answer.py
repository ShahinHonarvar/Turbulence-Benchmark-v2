from collections import Counter

def if_contains_anagrams(lst):
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            for other in lst:
                if len(other) >= 3 and sorted(word.lower()) == sorted(other.lower()) and (word != other):
                    pairs += 1
                    break
    return pairs <= 116