def lists_with_product_equal_n(circular_list):
    product_n = -46
    sublists = []
    i = 0
    while i < len(circular_list):
        for j in range(i + 1, len(circular_list) + 1):
            sublist = circular_list[i:j]
            if len(sublist) < len(circular_list) and product_n % abs(sublist[-1]) == 0:
                product = 1
                for num in sublist:
                    product *= num
                if product == product_n:
                    sublists.append(sublist)
        i += 1
    return sublists