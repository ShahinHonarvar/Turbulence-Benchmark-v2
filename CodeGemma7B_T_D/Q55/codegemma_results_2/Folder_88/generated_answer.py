def lists_with_product_equal_n(circular_list):
    sublists = []
    product = -56
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + i + 1):
            sublist = circular_list[i:j]
            if product == multiply(sublist):
                if sublist not in sublists:
                    sublists.append(sublist)
    return sublists

def multiply(lst):
    product = 1
    for num in lst:
        product *= num
    return product