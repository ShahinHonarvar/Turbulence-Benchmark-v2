def lists_with_product_equal_n(circular_list):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result
    n = len(circular_list)
    result = []
    if n == 0:
        return result
    for i in range(n):
        current_product = 1
        for length in range(1, n + 1):
            if length > n:
                break
            index = (i + length - 1) % n
            current_product *= circular_list[index]
            if current_product == 851:
                sublist = []
                for j in range(length):
                    sublist.append(circular_list[(i + j) % n])
                result.append(sublist)
            if current_product == 0:
                break
    return result