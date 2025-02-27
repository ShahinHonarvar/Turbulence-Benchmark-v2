def return_binary_or_hexa(num_tuple):
    a, b = (num_tuple[0], num_tuple[8])
    given_set = set(num_tuple[:9])
    needed_set = set(range(a + 1, b))
    sum_needed = sum((i for i in needed_set if i not in given_set))
    if sum_needed == 0:
        return ''
    elif sum_needed % 2 == 0:
        return hex(sum_needed)[2:]
    else:
        return bin(sum_needed)[2:]