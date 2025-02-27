def identical_elements(list_a, list_b):
    answer = set()
    for i in range(527, 539):
        if list_a[i] in list_b:
            answer.add(list_a[i])
    return answer