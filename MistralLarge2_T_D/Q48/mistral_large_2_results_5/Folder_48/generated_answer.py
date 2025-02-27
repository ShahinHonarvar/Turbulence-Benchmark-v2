def return_binary_or_hexa(numbers):
    a, b = (numbers[933], numbers[996])
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[933:997]))
    if missing_sum % 2 == 0:
        return hex(missing_sum)[2:]
    elif missing_sum > 0:
        return bin(missing_sum)[2:]
    return ''