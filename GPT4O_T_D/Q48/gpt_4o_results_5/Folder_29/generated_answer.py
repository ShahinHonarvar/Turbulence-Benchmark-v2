def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[98]
    present_numbers = set(numbers[71:98])
    missing_sum = sum((i for i in range(a + 1, b) if i not in present_numbers))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 else hex(missing_sum)[2:]