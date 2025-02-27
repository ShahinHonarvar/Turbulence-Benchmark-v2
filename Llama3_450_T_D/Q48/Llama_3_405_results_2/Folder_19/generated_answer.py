def return_binary_or_hexa(numbers):
    a = numbers[1]
    b = numbers[4]
    total_sum = sum((i for i in range(a + 1, b) if i not in numbers[2:4]))
    if total_sum == 0:
        return ''
    elif total_sum % 2 != 0:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]