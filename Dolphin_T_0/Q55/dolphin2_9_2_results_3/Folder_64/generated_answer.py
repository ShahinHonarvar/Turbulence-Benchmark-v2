def lists_with_product_equal_n(n, circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            if i == j:
                product = circular_list[i]
            else:
                product = 1
                for k in range(i, j):
                    product *= circular_list[k]
                product *= circular_list[j - 1]
            if product == n:
                result.append(circular_list[i:j])
    return result