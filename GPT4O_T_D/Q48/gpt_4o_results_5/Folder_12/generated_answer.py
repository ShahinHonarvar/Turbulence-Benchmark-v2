def return_binary_or_hexa(numbers):
    a = numbers[16]
    b = numbers[87]
    nums_in_range = set(numbers[17:87])
    missing_sum = sum((i for i in range(a + 1, b) if i not in nums_in_range))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]