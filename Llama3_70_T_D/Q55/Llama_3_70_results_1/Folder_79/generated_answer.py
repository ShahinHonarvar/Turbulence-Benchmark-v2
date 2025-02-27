def lists_with_product_equal_n(lst):
    n = len(lst)
    result = []
    for i in range(n):
        product = 1
        for j in range(n):
            product *= lst[(i + j) % n]
            if product == -83:
                result.append(lst[(i + j) % n])
            else:
                result.append(lst[(i + j) % n])
    final_result = []
    for i in range(len(result)):
        if result[i] == -83:
            final_result.append(result[i - n + 1:i + 1])
    return final_result