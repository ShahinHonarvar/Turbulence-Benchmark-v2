def return_binary_or_hexa(numbers):
    a, b = (numbers[72], numbers[93])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[72:94]))
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    elif missing_sum > 0:
        return hex(missing_sum)[2:]
    return ''