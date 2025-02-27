def if_contains_anagrams(lists):
    count = 0
    for i in range(len(lists)):
        for j in range(i + 1, len(lists)):
            if len(lists[i]) >= 3 and len(lists[j]) >= 3:
                list1 = list(lists[i].lower())
                list1.sort()
                list2 = list(lists[j].lower())
                list2.sort()
                if list1 == list2:
                    count += 1
    return count <= 69