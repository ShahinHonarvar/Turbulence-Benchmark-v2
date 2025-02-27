def return_binary_or_hexa(numbers):
    a = numbers[17]
    b = numbers[88]
    exclude_set = set(numbers[17:89])
    total_sum = sum((i for i in range(a + 1, b) if i not in exclude_set))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]