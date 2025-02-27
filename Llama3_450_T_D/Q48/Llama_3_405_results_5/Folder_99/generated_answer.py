def return_binary_or_hexa(numbers):
    a = numbers[427]
    b = numbers[669]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[427:669]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]