def lists_with_product_equal_n(lst):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result

    def get_sublists(lst, length):
        return [lst[i:i + length] for i in range(len(lst) - length + 1)] + [lst[i:] + lst[:length - len(lst) + i] for i in range(length - 1, 0, -1)]
    result = []
    for length in range(1, len(lst) + 1):
        for sublist in get_sublists(lst, length):
            if product(sublist) == -690:
                result.append(sublist)
    return result