def return_binary_or_hexa(numbers):
    a = numbers[50]
    b = numbers[92]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[50:93]))
    if missing_sum == 0:
        return ''
    if missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]