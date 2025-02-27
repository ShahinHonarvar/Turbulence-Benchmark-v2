def lists_with_product_equal_n(numbers):

    def is_sublist_valid(sublist):
        product = 1
        for num in sublist:
            product *= num
        return product == -20
    result = []
    for i in range(len(numbers)):
        for j in range(i, len(numbers)):
            sublist = numbers[i:j + 1]
            if is_sublist_valid(sublist):
                result.append(sublist)
    return result