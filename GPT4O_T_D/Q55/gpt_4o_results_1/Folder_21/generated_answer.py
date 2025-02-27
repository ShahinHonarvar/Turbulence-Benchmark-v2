def lists_with_product_equal_n(circular_list):
    target = 851
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        sublist = []
        for i in range(n):
            index = (start + i) % n
            product *= circular_list[index]
            sublist.append(circular_list[index])
            if product == target:
                result.append(sublist[:])
            if product == 0 or product > target:
                break
    return result