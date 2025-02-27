from collections import Counter
    from itertools import permutations

def if_contains_anagrams(strings):
    count = 0
    word_set = set()
    for word in strings:
        if len(word) >= 3:
            sorted_word = ''.join(sorted(word.lower()))
            word_set.add(sorted_word)
    for perm in permutations(word_set):
        if perm[0] not in perm[1:]:
            continue
        for word in perm:
            if perm.count(word) >= 2:
                count += 1
    return count <= 2