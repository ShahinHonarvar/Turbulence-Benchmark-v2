from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    pairs = 0
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            sorted_word = ''.join(sorted(word))
            if sorted_word not in count:
                count[sorted_word] = 1
            else:
                count[sorted_word] += 1
                pairs += 1
    return pairs <= 392