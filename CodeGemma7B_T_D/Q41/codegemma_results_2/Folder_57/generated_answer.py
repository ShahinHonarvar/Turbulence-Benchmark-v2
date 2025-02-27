from collections import defaultdict

def identical_elements(list1, list2):
    result = set()
    for i in range(27, 56):
        if list1[i] in list2[i]:
            result.add(list1[i])
    return result