def lists_with_product_equal_n(circular_list):
    n = 91
    result = []
    length = len(circular_list)
    for start in range(length):
        for end in range(start, start + length):
            current_sublist = []
            product = 1
            for i in range(start, end + 1):
                index = i % length
                current_element = circular_list[index]
                current_sublist.append(current_element)
                product *= current_element
                if product == n:
                    result.append(current_sublist.copy())
                elif product > n:
                    break
    return result