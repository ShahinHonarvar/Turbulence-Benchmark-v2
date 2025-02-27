from itertools import islice

def lists_with_product_equal_n(circular_list):

    def product(sublist):
        result = 1
        for num in sublist:
            result *= num
        return result
    n = 46
    length = len(circular_list)
    full_list = circular_list * 2
    result = []
    for start in range(length):
        for end in range(1, length + 1):
            sublist = list(islice(full_list, start, start + end))
            if product(sublist) == n:
                result.append(sublist)
    return result