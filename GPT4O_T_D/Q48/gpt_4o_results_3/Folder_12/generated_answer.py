def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    number_set = set(numbers[16:88])
    missing_numbers_sum = sum((x for x in range(a + 1, b) if x not in number_set))
    if missing_numbers_sum == 0:
        return ''
    if missing_numbers_sum % 2 == 1:
        return bin(missing_numbers_sum)[2:]
    else:
        return hex(missing_numbers_sum)[2:]