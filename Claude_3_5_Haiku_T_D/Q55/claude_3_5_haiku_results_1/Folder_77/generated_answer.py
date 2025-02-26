def lists_with_product_equal_n(circular_list):
    n = 632
    length = len(circular_list)
    result = []
    for start in range(length):
        for end in range(start, start + length):
            sublist = []
            current_product = 1
            for i in range(start, end + 1):
                index = i % length
                current_element = circular_list[index]
                sublist.append(current_element)
                current_product *= current_element
            if current_product == n:
                result.append(sublist)
    return result