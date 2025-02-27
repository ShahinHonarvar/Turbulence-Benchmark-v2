def return_binary_or_hexa(numbers):
    a = numbers[90]
    b = numbers[200]
    existing_numbers = set(numbers[91:200])
    total_sum = sum((i for i in range(a + 1, b) if i not in existing_numbers))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]