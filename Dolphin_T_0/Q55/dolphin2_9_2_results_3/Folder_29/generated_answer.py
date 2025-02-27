def lists_with_product_equal_n(numbers):
    if not numbers:
        return []
    n = len(numbers)
    result = []
    for length in range(1, n + 1):
        for i in range(n):
            product = 1
            sublist = []
            for j in range(i, i + length):
                sublist.append(numbers[j % n])
                product *= numbers[j % n]
            if product == 15:
                result.append(sublist)
    return result