def return_binary_or_hexa(numbers):
    a = numbers[450]
    b = numbers[905]
    missing = set(range(a + 1, b))
    present = set(numbers[451:905])
    absent_numbers = missing - present
    sum_absent = sum(absent_numbers)
    if sum_absent == 0:
        return ''
    if sum_absent % 2 == 1:
        return bin(sum_absent)[2:]
    else:
        return hex(sum_absent)[2:]