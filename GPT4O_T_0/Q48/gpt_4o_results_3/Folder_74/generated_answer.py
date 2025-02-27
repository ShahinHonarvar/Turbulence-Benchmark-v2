def return_binary_or_hexa(numbers):
    a = numbers[69]
    b = numbers[97]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[70:98]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]