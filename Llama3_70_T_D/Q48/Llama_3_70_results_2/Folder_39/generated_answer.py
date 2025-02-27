def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[44:92]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]