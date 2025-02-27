def return_binary_or_hexa(numbers):
    a = numbers[20]
    b = numbers[35]
    range_sum = sum((x for x in range(a + 1, b) if x not in numbers[21:36]))
    if range_sum == 0:
        return ''
    if range_sum % 2 == 1:
        return bin(range_sum)[2:]
    return hex(range_sum)[2:]