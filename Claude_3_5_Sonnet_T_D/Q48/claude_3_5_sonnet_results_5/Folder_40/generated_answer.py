def return_binary_or_hexa(t):
    a, b = (t[0], t[3])
    excluded_nums = set(t[0:4])
    sum_of_nums = sum((num for num in range(a + 1, b) if num not in excluded_nums))
    if sum_of_nums == 0:
        return ''
    elif sum_of_nums % 2 == 1:
        return bin(sum_of_nums)[2:]
    else:
        return hex(sum_of_nums)[2:].lstrip('0')