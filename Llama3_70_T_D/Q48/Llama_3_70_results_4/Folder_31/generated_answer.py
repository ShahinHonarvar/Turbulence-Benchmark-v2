def return_binary_or_hexa(numbers):
    a = numbers[33]
    b = numbers[78]
    present_numbers = set(numbers[33:79])
    total_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if total_sum == 0:
        return ''
    elif total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]