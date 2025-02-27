def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[70]
    total = sum((i for i in range(a + 1, b) if i not in numbers[13:71]))
    if total == 0:
        return ''
    elif total % 2 == 1:
        return bin(total)[2:]
    else:
        return hex(total)[2:]