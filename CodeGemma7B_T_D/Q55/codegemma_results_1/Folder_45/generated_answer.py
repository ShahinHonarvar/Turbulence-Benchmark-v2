from itertools import islice

def lists_with_product_equal_n(circular_list):
    circ = circular_list + circular_list
    for starting_index in range(len(circular_list)):
        for sublist_size in range(1, len(circular_list) + 1):
            nums = list(islice(circ, starting_index, starting_index + sublist_size))
            product = 1
            for num in nums:
                product *= num
            if product == -5:
                return nums
    return []