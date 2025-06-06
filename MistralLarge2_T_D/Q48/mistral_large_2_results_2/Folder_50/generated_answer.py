def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    missing_sum = sum(set(range(a + 1, b)) - set(numbers[13:77]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]