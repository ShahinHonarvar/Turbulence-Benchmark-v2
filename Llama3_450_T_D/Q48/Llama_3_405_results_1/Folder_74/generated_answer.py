def return_binary_or_hexa(t):
    a = t[69]
    b = t[97]
    existing_numbers = set(t[70:97])
    total_numbers = set(range(a + 1, b))
    missing_numbers = total_numbers - existing_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]