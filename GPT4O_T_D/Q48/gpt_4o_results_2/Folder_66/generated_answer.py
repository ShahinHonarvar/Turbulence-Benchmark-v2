def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    total_sum = sum((x for x in range(a + 1, b) if x not in numbers[12:76]))
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    return hex(total_sum)[2:]