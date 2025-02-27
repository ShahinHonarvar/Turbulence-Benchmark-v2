def lists_with_product_equal_n(numbers):
    n = len(numbers)
    result = []
    for i in range(n):
        product = 1
        for j in range(i, n):
            product *= numbers[j]
            if product == -5:
                result.append(numbers[i:j + 1])
            if product > -5:
                break
            if j == n - 1:
                for k in range(i):
                    product *= numbers[k]
                    if product == -5:
                        result.append(numbers[k:j + 1])
                    if product > -5:
                        break
    return result