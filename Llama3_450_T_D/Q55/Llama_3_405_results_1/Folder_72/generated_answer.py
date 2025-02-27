def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = 10
    result = []
    length = len(lst)
    if length == 0:
        return result
    for start in range(length):
        current_product = 1
        for end in range(start, start + length):
            current_product *= lst[end % length]
            if current_product == n:
                result.append(lst[start:end + 1])
            if current_product > n:
                break
    return result