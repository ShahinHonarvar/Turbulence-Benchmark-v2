def lists_with_product_equal_n(circular_list):

    def get_product(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product
    n = len(circular_list)
    result = []
    for start in range(n):
        product = 1
        for length in range(1, n + 1):
            product *= circular_list[(start + length - 1) % n]
            if product == 632:
                if start + length <= n:
                    result.append(circular_list[start:start + length])
                else:
                    part1 = circular_list[start:n]
                    part2 = circular_list[0:(start + length) % n]
                    result.append(part1 + part2)
    return result