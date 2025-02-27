from collections import Counter

def if_contains_anagrams(lists):
    count = 0
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if len(lists[i]) >= 3 and len(lists[j]) >= 3 and (Counter(lists[i].lower()) == Counter(lists[j].lower())):
                count += 1
    return count <= 407