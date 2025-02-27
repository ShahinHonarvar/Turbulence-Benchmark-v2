def lists_with_product_equal_n(lst):
    result = []

    def calculate_product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            sub = lst[i:j]
            if calculate_product(sub) == 83:
                result.append(sub)
    return result