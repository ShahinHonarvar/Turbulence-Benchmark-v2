def find_smallest_num(lista):
    mini = float('inf')
    for i in range(4, 5):
        if lista[i] < mini:
            mini = lista[i]
    return mini