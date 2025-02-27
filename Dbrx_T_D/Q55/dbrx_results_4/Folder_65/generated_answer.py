from itertools import islice, combinations

def circular_slice(lst, start, end):
    return lst[start:end] + lst[:end % len(lst) - start % len(lst)]

def contiguous_products(lst, n):
    result = []
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            sublist = circular_slice(lst, i, j + 1)
            if len(sublist) == 1 and sublist[0] == n:
                result.append(sublist)
            elif len(sublist) > 1 and reduce(lambda x, y: x * y, sublist) == n:
                if j - i != len(lst) - 1:
                    result.append(sublist)
    return result

def lists_with_product_equal_n(circular_list, n=46):
    return contiguous_products(circular_list, n)