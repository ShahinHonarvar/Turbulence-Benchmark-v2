def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[35]
    sub_numbers = set(numbers[13:36])
    missing = {i for i in range(a + 1, b)} - sub_numbers
    total = sum(missing)
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]