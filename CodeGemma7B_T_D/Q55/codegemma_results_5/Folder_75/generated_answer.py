def lists_with_product_equal_n(circular_list):
    result = []
    product = 1
    for element in circular_list:
        product *= element
    for i in range(len(circular_list)):
        end_product = product
        for j in range(i, len(circular_list)):
            end_product //= circular_list[j]
            if end_product == 13:
                sublist = circular_list[i:]
                if sublist not in result:
                    result.append(sublist)
    for i in range(len(circular_list)):
        start_product = product
        for j in range(i):
            start_product //= circular_list[j]
            if start_product == 13:
                sublist = circular_list[:i + 1]
                if sublist not in result:
                    result.append(sublist)
    return result