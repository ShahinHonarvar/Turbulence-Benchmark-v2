def identical_elements(listA, listB):
    answer = set()
    for i in range(62, 100):
        if listA[i] in listB:
            answer.add(listA[i])
    return answer