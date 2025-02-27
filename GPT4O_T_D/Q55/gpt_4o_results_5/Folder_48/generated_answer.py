def lists_with_product_equal_n(circular_list):

    def product_of_list(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    length = len(circular_list)
    result = []
    for i in range(length):
        for size in range(1, length + 1):
            sublist = []
            for j in range(size):
                sublist.append(circular_list[(i + j) % length])
            if product_of_list(sublist) == 990:
                result.append(sublist)
    return result