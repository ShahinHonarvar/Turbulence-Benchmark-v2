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
        current_list = []
        for end in range(start, start + n):
            current_element = circular_list[end % n]
            current_product *= current_element
            current_list.append(current_element)
            if current_product == 93:
                result.append(current_list[:])
            if len(current_list) == n:
                break
    return result