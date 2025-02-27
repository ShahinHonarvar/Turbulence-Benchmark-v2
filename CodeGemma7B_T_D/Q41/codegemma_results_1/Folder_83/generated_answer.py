def identical_elements(lst1, lst2):
    answer = set()
    for i in range(90, 201):
        if lst1[i] == lst2[i]:
            answer.add(lst1[i])
    return answer