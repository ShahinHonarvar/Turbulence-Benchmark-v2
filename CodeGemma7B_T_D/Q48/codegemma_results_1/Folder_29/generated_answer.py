def return_binary_or_hexa(sorted_tuple):
    a, b = (sorted_tuple[70], sorted_tuple[98])
    sum = 0
    for num in range(a + 1, b):
        if num not in sorted_tuple[70:99]:
            sum += num
    return bin(sum)[2:] if sum % 2 else hex(sum)[2:].upper()