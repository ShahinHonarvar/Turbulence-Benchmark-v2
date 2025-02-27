def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[450:906]))
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum == 0:
        return ''
    else:
        return hex(total_sum)[2:]