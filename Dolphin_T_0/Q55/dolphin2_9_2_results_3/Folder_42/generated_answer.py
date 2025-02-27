def lists_with_product_equal_n(n, circular_list):
    result = []
    for i in range(len(circular_list)):
        for j in range(i + 1, len(circular_list) + 1):
            if i == j:
                if circular_list[i] * circular_list[i + 1] == n:
                    result.append([circular_list[i], circular_list[i + 1]])
            elif circular_list[i:j] == circular_list[j:j + (j - i) + 1]:
                product = 1
                for k in circular_list[i:j]:
                    product *= k
                if product == n:
                    result.append(list(circular_list[i:j]))
    return result