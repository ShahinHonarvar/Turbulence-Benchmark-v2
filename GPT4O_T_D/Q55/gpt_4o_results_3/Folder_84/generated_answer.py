def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result_list = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = [circular_list[i % n] for i in range(start, end + 1)]
            if product(sublist) == -906:
                result_list.append(sublist)
            if len(sublist) >= n:
                break
    return result_list