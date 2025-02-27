def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for number in lst:
            result *= number
        return result
    n = len(circular_list)
    result_lists = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = circular_list[start:end + 1 if end < n else end - n + 1]
            if product(sublist) == 733:
                result_lists.append(sublist)
    return result_lists