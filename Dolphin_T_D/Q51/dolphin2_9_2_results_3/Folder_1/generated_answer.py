from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in count:
                count[sorted_word] = 1
            else:
                pairs += 1
        if pairs > 30:
            return False
    return pairs <= 30