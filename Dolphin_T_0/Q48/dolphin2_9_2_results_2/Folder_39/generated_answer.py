def return_binary_or_hexa(numbers):
    a = numbers[44]
    b = numbers[91]
    _sum = sum([x for x in range(a + 1, b) if x not in numbers[44:92]])
    if _sum % 2 != 0:
        return bin(_sum)[2:]
    else:
        return hex(_sum)[2:]