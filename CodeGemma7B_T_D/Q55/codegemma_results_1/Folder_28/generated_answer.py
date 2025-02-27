from itertools import islice, combinations_with_replacement

def lists_with_product_equal_n(list1):
    required_product = 85
    output_list = []
    list_length = len(list1)
    for i in range(0, list_length):
        tail_start_index = i
        for j in range(tail_start_index + 1, list_length + tail_start_index + 1):
            circular_tail = islice(list1, tail_start_index, j)
            head_start_index = j % list_length
            for k in range(head_start_index, list_length + head_start_index):
                circular_head = islice(list1, k, j)
                product = 1
                for element in circular_head:
                    product *= element
                if product == required_product:
                    output_list.append([element for element in circular_tail])
    return output_list