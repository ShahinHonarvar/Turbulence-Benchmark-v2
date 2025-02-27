def lists_with_product_equal_n(numbers):
    if -46 in numbers:
        return [[-46]] if numbers.count(-46) > 1 else [[]]
    n = len(numbers)
    sublists = []
    for i in range(n):
        product = 1
        j = i
        while product != -46 and j != i:
            product *= numbers[j]
            j = (j + 1) % n
            if product > -46:
                break
        if product != -46:
            continue
        sublists.append(list(numbers[i:j + 1]))
    return sublists