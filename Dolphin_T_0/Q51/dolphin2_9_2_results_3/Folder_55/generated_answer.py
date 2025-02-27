from collections import Counter

def if_contains_anagrams(lst):
    count_anagrams = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i]) >= 3 and len(lst[j]) >= 3 and (Counter(lst[i].lower()) == Counter(lst[j].lower())):
                count_anagrams += 1
    return count_anagrams <= 44