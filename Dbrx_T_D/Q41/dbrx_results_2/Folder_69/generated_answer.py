def identical_elements(list1, list2):
    result = set()
    for i in range(len(list1)):
        if i >= 32 and i <= 35:
            for j in range(len(list2)):
                if list1[i] == list2[j] and list1[i] not in result:
                    result.add(list1[i])
    return result