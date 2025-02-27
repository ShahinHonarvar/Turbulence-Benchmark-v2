def lists_with_product_equal_n(circular_list):
    N = len(circular_list)
    sublists = []
    for i in range(N):
        product = circular_list[i]
        j = i + 1
        while j % N != i:
            product *= circular_list[j % N]
            if product == 5:
                sublists.append(circular_list[i:j % N + 1])
            elif product > 5:
                break
            j += 1
    return sublists