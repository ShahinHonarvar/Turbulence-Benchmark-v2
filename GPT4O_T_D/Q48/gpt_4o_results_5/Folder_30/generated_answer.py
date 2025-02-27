def return_binary_or_hexa(numbers):
    a = numbers[22]
    b = numbers[24]
    missing_numbers = set(range(a + 1, b))
    tuple_numbers = set(numbers[23:24])
    missing_sum = sum(missing_numbers - tuple_numbers)
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]