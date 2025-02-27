def return_binary_or_hexa(numbers):
    a = numbers[55]
    b = numbers[84]
    num_set = set(numbers[56:84])
    missing_sum = sum((n for n in range(a + 1, b) if n not in num_set))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]