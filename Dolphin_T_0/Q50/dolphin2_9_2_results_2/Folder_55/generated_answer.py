from collections import Counter

def if_contains_anagrams(lst):
    count = Counter()
    for word in lst:
        if len(word) >= 3:
            count[tuple(sorted(word.lower()))] += 1
            if count[tuple(sorted(word.lower()))] == 2:
                if sum(count.values()) >= 15:
                    return True
    return False