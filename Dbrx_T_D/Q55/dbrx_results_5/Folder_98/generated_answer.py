from itertools import islice, cycle

def lists_with_product_equal_n(circular_list):
    n = -1
    result = []
    prefix = [1]
    for i in range(len(circular_list)):
        prefix = [x * circular_list[i] % n for x in prefix]
        prefix.append(prefix[-1] * circular_list[i] % n)
        sublists = [list(sublist) for sublist in (sub(prefix, k) for k in range(1, len(prefix))) if all((x == n for x in sub(sublist, 1)[0]))]
        result.extend(sublists)
    return result

def sub(iterable, n):
    """Return n length subsequences of elements from the input iterable in reverse."""
    return reversed(list(islice(zip(*[iter(iterable)] * n), n)))