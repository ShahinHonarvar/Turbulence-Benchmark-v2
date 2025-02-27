def return_binary_or_hexa(numbers):
    a = numbers[15]
    b = numbers[57]
    numbers_between = [numbers[i] for i in range(15, 58)]
    missing = [num for num in range(a + 1, b) if num not in numbers_between]
    if not missing:
        return ''
    total = sum(missing)
    if total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]