from itertools import islice

def circular_iter(lst):
    while True:
        for item in lst:
            yield item

def sublists_with_product_equal_n(lst, n):
    circular_lst = list(lst)
    result = []
    head = 0
    tail = 0
    for i in range(len(circular_lst)):
        head = (head + 1) % len(circular_lst)
        tail = (tail + 1) % len(circular_lst)
        sublist = list(islice(circular_iter(circular_lst), head, tail))
        if len(sublist) > 1:
            if all((isinstance(x, int) for x in sublist)) and sublist[0] * nth_product(sublist[1:], n) == n:
                result.append(sublist)
    return result

def nth_product(lst, n):
    if not lst or n == 0:
        return 1
    return lst[0] * nth_product(lst[1:], n - 1) if lst[-1] == 1 else lst[0] * nth_product(lst[1:], n)