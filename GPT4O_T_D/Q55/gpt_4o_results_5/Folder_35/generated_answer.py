def lists_with_product_equal_n(circular_list):

    def product_of_sublist(lst):
        product = 1
        for num in lst:
            product *= num
        return product
    length = len(circular_list)
    result = []
    for i in range(length):
        for j in range(1, length + 1):
            sublist = []
            for k in range(j):
                index = (i + k) % length
                sublist.append(circular_list[index])
            if product_of_sublist(sublist) == 83:
                result.append(sublist)
    return result