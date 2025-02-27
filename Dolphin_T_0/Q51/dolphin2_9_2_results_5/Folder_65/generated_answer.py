from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    pairs = {}
    for word in lst:
        if len(word) >= 3:
            word = word.lower()
            counter = Counter(word)
            key = ''.join(sorted(counter.keys()))
            if key in pairs:
                pairs[key].append(word)
            else:
                pairs[key] = [word]
    for key in pairs:
        if len(pairs[key]) >= 2:
            count += len(pairs[key]) * (len(pairs[key]) - 1) // 2
    if count <= 72:
        return True
    else:
        return False