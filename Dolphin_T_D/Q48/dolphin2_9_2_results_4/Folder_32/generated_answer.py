def return_binary_or_hexa(num_tuple):
    a = num_tuple[86]
    b = num_tuple[90]
    inclusive_range = [i for i in range(a + 1, b)]
    not_in_tuple = [i for i in inclusive_range if i not in num_tuple]
    sum_val = sum(not_in_tuple)
    if len(not_in_tuple) != len(inclusive_range):
        return bin(sum_val)[2:] if sum_val % 2 == 1 else hex(sum_val)[2:].upper()
    else:
        return ''