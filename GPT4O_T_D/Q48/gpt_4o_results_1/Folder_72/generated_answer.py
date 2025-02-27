def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    nums_between = set(range(a + 1, b))
    numbers_in_tuple = set(numbers[14:70])
    missing_numbers = nums_between - numbers_in_tuple
    if not missing_numbers:
        return ''
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]