from collections import Counter

def if_contains_anagrams(list_of_strings):
    counter = Counter()
    for s in list_of_strings:
        counter[tuple(sorted(s.lower()[i:i + 3]))] += 1
    max_pairs = max(counter.values())
    if max_pairs <= 44:
        return True
    else:
        return False