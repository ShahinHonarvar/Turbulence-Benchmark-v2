from collections import Counter

def if_contains_anagrams(lst):
    count = {}
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word not in count:
                count[sorted_word] = 1
            else:
                count[sorted_word] += 1
    pairs = sum((n * (n - 1) // 2 for n in count.values()))
    if pairs <= 206:
        return True
    else:
        return False