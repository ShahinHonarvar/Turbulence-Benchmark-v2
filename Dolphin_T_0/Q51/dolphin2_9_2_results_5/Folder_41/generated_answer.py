from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            if sorted_word in count:
                count[sorted_word] += 1
            else:
                count[sorted_word] = 1
    num_pairs = sum((v * (v - 1) // 2 for v in count.values() if v > 1))
    return num_pairs <= 52