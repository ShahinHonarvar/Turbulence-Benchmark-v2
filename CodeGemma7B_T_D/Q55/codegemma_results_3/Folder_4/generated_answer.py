def lists_with_product_equal_n(circular_list):
    N = len(circular_list)
    for i in range(N):
        for j in range(i + 1, N + 1):
            sublist = circular_list[i:j]
            if len(sublist) <= j - i and product(sublist) == 91:
                yield sublist

def product(list):
    prod = 1
    for i in list:
        prod *= i
    return prod