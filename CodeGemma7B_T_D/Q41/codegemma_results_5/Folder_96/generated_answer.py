from collections import Counter

def identical_elements(list1, list2):
    same = set()
    for i in range(50, 201):
        if list1[i] == list2[i]:
            same.add(list1[i])
    return same