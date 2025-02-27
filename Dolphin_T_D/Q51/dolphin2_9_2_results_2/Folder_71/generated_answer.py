from collections import Counter

def if_contains_anagrams(lst):
    pair_count = 0
    check_anagrams = set()
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            pair_1 = ''.join(sorted(lst[i].lower()))
            pair_2 = ''.join(sorted(lst[j].lower()))
            if len(pair_1) >= 3 and len(pair_2) >= 3 and (Counter(pair_1) == Counter(pair_2)):
                if (pair_1, pair_2) in check_anagrams or (pair_2, pair_1) in check_anagrams:
                    continue
                else:
                    check_anagrams.add((pair_1, pair_2))
                    pair_count += 1
                    if pair_count > 9:
                        return False
    return True