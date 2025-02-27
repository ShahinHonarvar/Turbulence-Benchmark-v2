def lists_with_product_equal_n(circular_list):
    result = []
    k = len(circular_list)
    for i in range(k):
        for j in range(2, min(i + 10, k - i + 1)):
            product = 1
            for sublist in range(j):
                product *= circular_list[(i + sublist) % k]
            if product == 15:
                new_list = []
                for sublist in range(j):
                    new_list.append((i + sublist) % k)
                if new_list not in result:
                    result.append(new_list)
    return result