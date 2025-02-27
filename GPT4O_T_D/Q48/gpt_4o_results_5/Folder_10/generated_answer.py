def return_binary_or_hexa(t):
    a = t[36]
    b = t[54]
    expected_numbers = set(range(a + 1, b))
    existing_numbers = set(t[37:54])
    missing_numbers = expected_numbers - existing_numbers
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]