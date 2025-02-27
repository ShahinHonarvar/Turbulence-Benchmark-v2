from itertools import islice

def lists_with_product_equal_n(lst):

    def is_contiguous_sublist(sublist):
        product = 1
        for num in sublist:
            product *= num
            if product > n:
                return False
        return product == n
    n = 91
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = list(islice(circular_list(lst, i), j - i + 1))
            if is_contiguous_sublist(sublist):
                result.append(sublist)
    return result

def circular_list(lst, start):
    while True:
        yield lst[start]
        start = (start + 1) % len(lst)