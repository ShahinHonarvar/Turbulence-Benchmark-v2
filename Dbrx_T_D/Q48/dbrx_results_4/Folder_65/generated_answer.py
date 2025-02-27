def return_binary_or_hexa(numbers):
    a = numbers[51]
    b = numbers[76]
    missing_numbers = [i for i in range(a + 1, b) if i not in numbers[51:77]]
    if not missing_numbers:
        return ''
    number_sum = sum(missing_numbers)
    if number_sum % 2:
        return bin(number_sum)[2:]
    else:
        return hex(number_sum)[2:].upper()