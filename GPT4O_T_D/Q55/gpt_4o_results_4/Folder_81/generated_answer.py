def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    for start in range(n):
        current_product = 1
        for end in range(start, start + n):
            current_product *= circular_list[end % n]
            if current_product == -8:
                sublist_length = end - start + 1
                result.append([circular_list[i % n] for i in range(start, start + sublist_length)])
            if sublist_length == n:
                break
    return result