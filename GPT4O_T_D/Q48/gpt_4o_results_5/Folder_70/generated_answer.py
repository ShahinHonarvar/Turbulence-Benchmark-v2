def return_binary_or_hexa(numbers):
    a = numbers[43]
    b = numbers[70]
    num_set = set(numbers[44:70])
    missing_sum = sum((i for i in range(a + 1, b) if i not in num_set))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    return hex(missing_sum)[2:]