def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    length = len(circular_list)
    result = []
    for start in range(length):
        for size in range(1, length + 1):
            sublist = [circular_list[(start + i) % length] for i in range(size)]
            if product(sublist) == -83:
                result.append(sublist)
    return result