def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n + i):
            product *= numbers[j % n]
            if product == 8 and [numbers[j % n] for j in range(i, n + i)] not in result:
                result.append([numbers[j % n] for j in range(i, n + i)])
    return result