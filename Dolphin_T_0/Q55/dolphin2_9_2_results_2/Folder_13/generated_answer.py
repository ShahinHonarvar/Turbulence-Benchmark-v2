from itertools import islice

def num_of_zeros(arr):
    return arr.count(0)

def num_of_ones(arr):
    return arr.count(1)

def complement(arr):
    return [1 - i for i in arr]

def lists_with_product_equal_n(circular_list):
    list_length = len(circular_list)
    if list_length == 0:
        return []
    head = circular_list[0]
    tail = circular_list[-1]
    if head != 1 and tail != 1:
        for i in range(1, list_length):
            if circular_list[i] != 1:
                head, tail = (tail, circular_list[i])
    com_list = complement(circular_list)
    total_ones_in_list = num_of_ones(circular_list) + num_of_zeros(circular_list)
    surplus_ones = num_of_ones(circular_list) - num_of_ones(circular_list // 2)
    result = [list(islice(circular_list, i, i + total_ones_in_list - surplus_ones)) for i in range(list_length)]
    return result