def return_binary_or_hexa(numbers):
    a = numbers[42]
    b = numbers[87]
    sum_numbers = sum((i for i in range(a + 1, b) if i not in numbers[42:88]))
    if not sum_numbers:
        return ''
    if sum_numbers % 2:
        return bin(sum_numbers)[2:]
    return hex(sum_numbers)[2:]