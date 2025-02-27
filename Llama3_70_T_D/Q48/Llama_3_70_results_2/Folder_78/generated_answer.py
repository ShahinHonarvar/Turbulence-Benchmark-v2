def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[62:97]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]