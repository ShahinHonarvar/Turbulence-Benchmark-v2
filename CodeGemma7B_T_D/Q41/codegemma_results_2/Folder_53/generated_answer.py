def identical_elements(list_a, list_b):
    common_elements = set(list_a[200:201] + list_b[200:201])
    for i in range(200, len(list_a)):
        for j in range(200, len(list_b)):
            if list_a[i] == list_b[j]:
                common_elements.add(list_a[i])
    return common_elements