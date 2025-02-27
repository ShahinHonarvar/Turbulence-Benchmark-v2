from itertools import permutations 

def lists_with_product_equal_n(circular_list):
    n = -82
    lists_of_contiguous_nums = []
    for i in range(len(circular_list)):
        start_index = i
        product = circular_list[i]
        current_size = 1
        j = (i + 1) % len(circular_list)
        while product == n:
            lists_of_contiguous_nums.append(circular_list[i:j + 1])
            if current_size >= len(circular_list):
                break
            product *= circular_list[j]
            current_size += 1
            j = (j + 1) % len(circular_list)
        product /= circular_list[start_index]
        current_size -= 1
        j = (i + current_size) % len(circular_list)
    return lists_of_contiguous_nums