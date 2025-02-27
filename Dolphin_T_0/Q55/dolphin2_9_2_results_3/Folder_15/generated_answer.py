def lists_with_product_equal_n(numbers):
    result = []
    for i in range(len(numbers)):
        for j in range(i + 2, len(numbers) + 1):
            if j - i <= len(numbers):
                product = 1
                for k in range(i, j):
                    product *= numbers[k % len(numbers)]
                if product == -7:
                    result.append(numbers[i:j])
    return result