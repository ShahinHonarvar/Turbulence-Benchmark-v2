import itertools

def if_contains_anagrams(lst):
    count = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (sorted(lst[i].lower()) == sorted(lst[j].lower())):
                count += 1
                if count > 30:
                    return False
    return count <= 30