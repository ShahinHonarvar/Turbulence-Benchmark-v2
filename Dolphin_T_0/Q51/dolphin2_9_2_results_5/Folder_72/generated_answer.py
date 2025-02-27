from collections import Counter

def if_contains_anagrams(a_list):
    pairs = 0
    for i in range(len(a_list)):
        for j in range(i + 1, len(a_list)):
            if len(a_list[i]) >= 3 and len(a_list[j]) >= 3:
                c1 = Counter(a_list[i].lower())
                c2 = Counter(a_list[j].lower())
                if c1 == c2:
                    pairs += 1
                    if pairs > 188:
                        return False
    return pairs <= 188