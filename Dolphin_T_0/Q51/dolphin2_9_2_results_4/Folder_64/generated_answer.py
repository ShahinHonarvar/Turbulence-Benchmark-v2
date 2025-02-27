from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    checked_pairs = set()
    groups = {}
    for word in lst:
        word = word.lower()
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word))
            if sorted_word not in groups:
                groups[sorted_word] = []
            groups[sorted_word].append(word)
    for group in groups.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if (group[i], group[j]) not in checked_pairs and (group[j], group[i]) not in checked_pairs:
                        checked_pairs.add((group[i], group[j]))
                        count += 1
    return count <= 59