def lists_with_product_equal_n(lst):
    result = []
    for length in range(len(lst) + 1):
        for i in range(len(lst)):
            if i + length <= len(lst):
                subset = lst[i:i + length]
                product = 1
                for number in subset:
                    product *= number
                if product == -54:
                    result.append(subset)
    return result