def return_binary_or_hexa(numbers):
    a = numbers[11]
    b = numbers[76]
    missing_numbers = set(range(a + 1, b)).difference(numbers[12:76])
    total_sum = sum(missing_numbers)
    if total_sum == 0:
        return ''
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    else:
        return hex(total_sum)[2:]