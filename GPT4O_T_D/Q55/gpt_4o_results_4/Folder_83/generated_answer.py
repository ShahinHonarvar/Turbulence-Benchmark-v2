def lists_with_product_equal_n(circular_list, n=-57):
    result = []
    length = len(circular_list)

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    for start in range(length):
        for end in range(1, length + 1):
            indices = [(start + i) % length for i in range(end)]
            sublist = [circular_list[i] for i in indices]
            if product(sublist) == n:
                result.append(sublist)
    return result