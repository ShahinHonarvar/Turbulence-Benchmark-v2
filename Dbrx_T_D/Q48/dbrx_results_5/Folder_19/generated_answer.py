def return_binary_or_hexa(tup):
    a, b = (tup[1], tup[4])
    sum_all = sum(range(a + 1, b))
    present_in_range = sum((num in t if a < num < b else False for t in (tup[:1], tup[4:])))
    if present_in_range < sum_all:
        sum_not_present = sum_all - present_in_range
        return '{:b}'.format(sum_not_present) if sum_not_present % 2 else '{:x}'.format(sum_not_present)
    elif present_in_range > sum_all:
        raise ValueError('All integers from a + 1 to b - 1 (both inclusive) are present in the specified range in the tuple')
    else:
        return ''