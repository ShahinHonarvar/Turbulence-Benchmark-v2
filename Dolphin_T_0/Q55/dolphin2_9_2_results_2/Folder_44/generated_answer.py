def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    product_29 = 29
    product_sofar = 1
    for i in range(n * 2 - 1):
        product_sofar = product_sofar * numbers[i % n]
        if product_sofar != product_29:
            result = [[numbers[(i - j) % n] for j in range(i % n + 1, n)]]
        elif result == []:
            result = [[numbers[(i - j) % n] for j in range(i % n + 1)]]
        elif result != []:
            result.append([numbers[(i - j) % n] for j in range(i % n + 1)])
    return result