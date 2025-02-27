def lists_with_product_equal_n(num_list):
    result = []
    size = len(num_list)
    for i in range(size):
        if num_list[i] == 28:
            result.append([28])
        else:
            product = num_list[i]
            for j in range(i + 1, size + 1):
                product *= num_list[j % size]
                if product == 28:
                    result.append(num_list[i:j % size + 1])
                elif product > 28:
                    break
    return result