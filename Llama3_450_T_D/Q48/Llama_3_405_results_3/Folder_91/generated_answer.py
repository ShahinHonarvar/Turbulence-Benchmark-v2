def return_binary_or_hexa(t):
    a, b = (t[0], t[6])
    absent_numbers = set(range(a + 1, b)) - set(t[1:6])
    total_sum = sum(absent_numbers)
    if not absent_numbers:
        return ''
    return bin(total_sum)[2:] if total_sum % 2 else hex(total_sum)[2:]