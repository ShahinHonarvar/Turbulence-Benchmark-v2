def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(1, length + 1):
            sublist = []
            for k in range(end):
                sublist.append(circular_list[(start + k) % length])
            if product_of_list(sublist) == 45:
                result.append(sublist)
    return result