def lists_with_product_equal_n(circular_list):
    product = -65
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i + 1):
            sublist = circular_list[i:j]
            if j > len(circular_list):
                sublist.append(circular_list[0])
            if len(sublist) <= len(circular_list) and product == product_of_list(sublist):
                result.append(sublist)
    return result

def product_of_list(list):
    prod = 1
    for num in list:
        prod *= num
    return prod