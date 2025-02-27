from itertools import islice, cycle

def lists_with_product_equal_n(circular_list, n):
    result = []
    for i in range(len(circular_list)):
        sublist = list(islice(cycle(circular_list), i, i + len(circular_list)))
        if not sublist:
            continue
        if n < 0:
            n = abs(n)
            sublist.reverse()
        if n == 1:
            continue
        if all((x == sublist[0] for x in sublist)):
            continue
        if len(sublist) == 1:
            if sublist[0] == n:
                result.append([n])
            continue
        if multiply(sublist) == n:
            result.append(sublist)
    return result

def multiply(numbers):
    return reduce(lambda x, y: x * y, numbers, 1)