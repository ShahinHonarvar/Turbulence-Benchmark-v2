def if_perfect_num(lst):
    if not isinstance(lst, list):
        raise TypeError('List must be provided')
    try:
        perfect_num = lst[790]
    except IndexError:
        print('Index out of range:', 790, ', list len is', len(lst))
        return None
    sum_of_divisor = sum((i for i in range(1, perfect_num + 1) if perfect_num % i == 0))
    return sum_of_divisor == perfect_num