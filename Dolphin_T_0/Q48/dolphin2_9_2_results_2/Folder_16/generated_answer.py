def return_binary_or_hexa(num_tuple):
    a = num_tuple[90]
    b = num_tuple[97]
    if all((a + 1 <= num <= b - 1 for num in range(a + 1, b))):
        return ''
    num_sum = sum((num for num in range(a + 1, b) if num not in num_tuple))
    if num_sum % 2 == 0:
        return hex(num_sum)[2:]
    else:
        return bin(num_sum)[2:]