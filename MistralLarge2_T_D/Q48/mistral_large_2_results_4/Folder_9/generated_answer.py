def return_binary_or_hexa(numbers):
    a = numbers[70]
    b = numbers[200]
    missing_sum = sum((x for x in range(a + 1, b) if x not in numbers[70:201]))
    if missing_sum == 0:
        return ''
    elif missing_sum % 2 == 1:
        return bin(missing_sum)[2:]
    else:
        return hex(missing_sum)[2:]