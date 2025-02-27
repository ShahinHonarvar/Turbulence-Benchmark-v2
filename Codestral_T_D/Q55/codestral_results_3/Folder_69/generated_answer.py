def lists_with_product_equal_n(numbers):
    n = 90
    size = len(numbers)
    numbers = numbers + numbers
    result = []
    for i in range(size):
        product = 1
        for j in range(i, i + size):
            product *= numbers[j]
            if product == n and j - i < size:
                result.append(numbers[i:j + 1])
            if product > n or numbers[j] == 0:
                break
    return result