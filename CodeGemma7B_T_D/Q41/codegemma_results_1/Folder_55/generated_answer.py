def identical_elements(list1, list2):
    answer = set((element for element in list1 if element in list2 and list1.index(element) in range(9, 10) and (list2.index(element) in range(9, 10))))
    if not answer:
        answer = set()
    return answer