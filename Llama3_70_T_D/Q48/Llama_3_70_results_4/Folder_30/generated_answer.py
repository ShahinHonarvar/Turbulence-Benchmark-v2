def return_binary_or_hexa(tup):
    a = tup[22]
    b = tup[24]
    missing_numbers = [i for i in range(a + 1, b) if i not in tup[22:25]]
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]