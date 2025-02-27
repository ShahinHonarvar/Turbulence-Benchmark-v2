def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[97]
    missing_numbers = set(range(a + 1, b)) - set(numbers[10:97])
    total_sum = sum(missing_numbers)
    if total_sum % 2 == 1:
        return bin(total_sum)[2:]
    elif total_sum > 0:
        return hex(total_sum)[2:]
    else:
        return ''