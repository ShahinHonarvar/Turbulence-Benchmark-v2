def return_binary_or_hexa(tup):
    a = tup[55]
    b = tup[84]
    excluded_nums = set(tup[55:85])
    total_sum = sum((num for num in range(a + 1, b) if num not in excluded_nums))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:].rstrip('L')