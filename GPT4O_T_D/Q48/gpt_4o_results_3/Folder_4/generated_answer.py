def return_binary_or_hexa(numbers):
    a = numbers[49]
    b = numbers[74]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[50:74]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    else:
        return bin(missing_sum)[2:]