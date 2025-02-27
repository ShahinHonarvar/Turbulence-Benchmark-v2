def return_binary_or_hexa(numbers):
    a = numbers[0]
    b = numbers[4]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[1:4]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 != 0 else hex(missing_sum)[2:]