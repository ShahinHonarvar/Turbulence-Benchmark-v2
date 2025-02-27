def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[12]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[11:12]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]