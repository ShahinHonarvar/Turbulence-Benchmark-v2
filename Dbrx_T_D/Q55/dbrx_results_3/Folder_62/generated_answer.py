from itertools import islice

def circular_list_generator(lst):
    while True:
        yield lst
        lst = lst[1:] + lst[:1]

def sublists_with_product_equal_n(lst, n):
    result = []
    for i in range(len(lst)):
        sub_list = list(islice(circular_list_generator(lst), i + 1))
        if sub_list and int(''.join(map(str, sub_list))) == n:
            result.append(sub_list)
    return result