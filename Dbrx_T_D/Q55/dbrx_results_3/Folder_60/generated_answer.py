from itertools import islice

def circular_list_to_array(circular_list):
    array = list(circular_list)
    return array + [array[0]]

def lists_with_product_equal_n(array, n=49):
    sublists = []
    product = 1
    current_sublist = []
    for i, element in enumerate(array):
        product *= element
        current_sublist.append(element)
        while product >= n:
            product //= current_sublist[0]
            del current_sublist[0]
        if product == n:
            sublists.append(current_sublist.copy())
    product = 1
    current_sublist = []
    for i in range(len(array) - 1, -1, -1):
        element = circular_list_to_array(array)[i]
        product *= element
        current_sublist.append(element)
        while product >= n and current_sublist:
            product //= current_sublist[0]
            del current_sublist[0]
        if product == n:
            sublists.append(current_sublist[::-1])
    return sublists