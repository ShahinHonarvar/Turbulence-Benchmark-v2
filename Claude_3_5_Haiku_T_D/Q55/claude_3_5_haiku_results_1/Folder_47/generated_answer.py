def lists_with_product_equal_n(circular_list):
    n = len(circular_list)
    result = []
    for start in range(n):
        for end in range(start, start + n):
            sublist = []
            product = 1
            for i in range(start, end + 1):
                current_index = i % n
                element = circular_list[current_index]
                sublist.append(element)
                product *= element
            if product == -94:
                result.append(sublist)
    return result