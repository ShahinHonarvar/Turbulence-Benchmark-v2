from itertools import islice, cycle

def lists_with_product_equal_n(lst):

    def product(lst):
        result = 1
        for num in lst:
            result *= num
        return result

    def circular_slice(lst, start, length):
        return [x for i, x in enumerate(islice(cycle(lst), start, start + length))]
    n = 990
    circular_lst = cycle(lst)
    length = len(lst)
    result = []
    for i in range(length):
        for j in range(i, length):
            sublst = circular_slice(circular_lst, i, j - i + 1)
            if product(sublst) == n:
                result.append(sublst)
    return result