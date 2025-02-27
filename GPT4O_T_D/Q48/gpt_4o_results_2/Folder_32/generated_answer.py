def return_binary_or_hexa(numbers):
    a = numbers[86]
    b = numbers[90]
    expected_sum = sum(range(a + 1, b))
    actual_sum = sum((x for x in range(a + 1, b) if x not in numbers[87:90]))
    if actual_sum == expected_sum:
        return ''
    if actual_sum % 2 == 1:
        return bin(actual_sum)[2:]
    else:
        return hex(actual_sum)[2:]