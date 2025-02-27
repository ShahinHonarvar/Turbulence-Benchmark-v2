from collections import Counter

def if_contains_anagrams(strings):
    pairs = 0
    for i in range(len(strings)):
        for j in range(i + 1, len(strings)):
            if len(strings[i]) < 3 or len(strings[j]) < 3:
                continue
            if Counter(strings[i].lower()) == Counter(strings[j].lower()):
                pairs += 1
    return pairs >= 9