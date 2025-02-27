from collections import Counter

def if_contains_anagrams(lst):
    c = Counter()
    for word in lst:
        c[tuple(sorted(word.lower()))] += 1
    count = 0
    for key in c:
        if c[key] > 1 and len(key) >= 3:
            count += c[key]
            if count >= 79:
                return True
    return count >= 79