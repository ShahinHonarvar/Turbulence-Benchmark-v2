def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start + 1, n + 1):
            sublist = circular_list[start:end]
            if product(sublist) == 51:
                result.append(sublist)
        if n > 1:
            for end in range(0, start):
                sublist = circular_list[start:] + circular_list[:end + 1]
                if product(sublist) == 51:
                    result.append(sublist)
    return result