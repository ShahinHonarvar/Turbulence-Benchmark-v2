from collections import Counter

def if_contains_anagrams(s):
    count = 0
    seen_pairs = set()
    for word in s:
        if len(word) < 3:
            continue
        word = word.lower()
        if sorted(word) in seen_pairs:
            count += 1
            seen_pairs.remove(sorted(word))
        else:
            seen_pairs.add(sorted(word))
    return count <= 64