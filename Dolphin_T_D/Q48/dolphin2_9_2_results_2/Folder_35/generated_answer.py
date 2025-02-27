def return_binary_or_hexa(numbers):
    a = numbers[77]
    b = numbers[84]
    if all((i in numbers for i in range(a + 1, b))):
        return ''
    missing_sum = sum(set(range(a, b + 1)) - set(numbers[77:85]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]