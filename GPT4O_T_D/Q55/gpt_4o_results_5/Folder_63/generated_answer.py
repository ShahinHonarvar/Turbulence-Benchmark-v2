def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    circular_list += circular_list[:-1]
    result = []
    for i in range(n):
        for j in range(i + 1, i + n + 1):
            sublist = circular_list[i:j]
            if product(sublist) == 96:
                result.append(sublist)
    return result