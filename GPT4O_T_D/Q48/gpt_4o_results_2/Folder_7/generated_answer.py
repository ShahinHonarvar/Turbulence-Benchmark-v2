def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[97]
    required_sum = sum((i for i in range(a + 1, b) if i not in numbers[11:97]))
    if required_sum == 0:
        return ''
    if required_sum % 2 == 1:
        return bin(required_sum)[2:]
    else:
        return hex(required_sum)[2:]