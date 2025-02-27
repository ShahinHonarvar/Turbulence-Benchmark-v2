def lists_with_product_equal_n(circular_list):

    def product(sublist):
        prod = 1
        for num in sublist:
            prod *= num
        return prod
    n = len(circular_list)
    result = []
    for i in range(n):
        for j in range(1, n + 1):
            if j <= n:
                current_list = circular_list[i:i + j]
            else:
                current_list = circular_list[i:n] + circular_list[0:j - (n - i)]
            if product(current_list) == -41:
                result.append(current_list)
    return result