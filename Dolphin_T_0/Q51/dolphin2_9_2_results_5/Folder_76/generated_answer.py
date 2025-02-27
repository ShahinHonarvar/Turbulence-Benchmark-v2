from collections import Counter

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        if len(lst[i]) >= 3:
            sorted_i = Counter(lst[i].lower())
            for j in range(i + 1, len(lst)):
                if len(lst[j]) >= 3 and sorted_i == Counter(lst[j].lower()):
                    count += 1
                    if count >= 91:
                        return True
    return False