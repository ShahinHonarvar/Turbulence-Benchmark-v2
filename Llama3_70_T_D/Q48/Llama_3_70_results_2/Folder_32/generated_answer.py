def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[86:91]))
    if total_sum == 0:
        return ''
    if total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]