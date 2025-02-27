def return_binary_or_hexa(numbers):
    a = numbers[25]
    b = numbers[80]
    missing_numbers = set(range(a + 1, b))
    tuple_numbers = set(numbers[26:80])
    missing_sum = sum(missing_numbers - tuple_numbers)
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]