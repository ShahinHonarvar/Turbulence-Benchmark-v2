def lists_with_product_equal_n(circular_list):
    sublists = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            sublists.append(circular_list[i:j])
    sublists.sort(key=lambda x: multiply(x))
    sublists_with_product_n = []
    for sublist in sublists:
        if multiply(sublist) == 85:
            sublists_with_product_n.append(sublist)
    return sublists_with_product_n

def multiply(int_list):
    product = 1
    for num in int_list:
        product *= num
    return product