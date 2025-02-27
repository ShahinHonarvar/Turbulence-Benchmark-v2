def identical_elements(list_A, list_B):
    common_elements = set()
    for i in range(31, 35):
        if list_A[i] == list_B[i]:
            common_elements.add(list_A[i])
    return common_elements