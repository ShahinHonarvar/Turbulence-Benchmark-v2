def return_binary_or_hexa(numbers):
    a = numbers[10]
    b = numbers[76]
    missing_sum = sum((i for i in range(a + 1, b) if i not in numbers[11:76]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 != 0:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]