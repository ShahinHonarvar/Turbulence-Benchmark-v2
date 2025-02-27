from collections import defaultdict

def if_contains_anagrams(lst):
    count = 0
    processed = defaultdict(int)
    for word in lst:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            processed[sorted_word] += 1
    for value in processed.values():
        if value > 1:
            count += value * (value - 1) // 2
        if count > 401:
            return False
    return True