def lists_with_product_equal_n(numbers):
    n = len(numbers)
    numbers = numbers + numbers
    result = []
    for i in range(n):
        product = 1
        sublist = []
        for j in range(i, i + n):
            product *= numbers[j]
            sublist.append(numbers[j])
            if product == 733:
                result.append(sublist)
            elif product > 733:
                break
    return result