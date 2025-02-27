def lists_with_product_equal_n(n, circular_list):
    result = []
    size = len(circular_list)
    for i in range(size):
        temp = [circular_list[i]]
        product = circular_list[i]
        j = (i + 1) % size
        while j != i:
            temp.append(circular_list[j])
            product *= circular_list[j]
            if product == n:
                result.append(temp)
            elif product > n:
                break
            j = (j + 1) % size
    return result