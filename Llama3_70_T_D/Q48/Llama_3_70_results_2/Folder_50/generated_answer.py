def return_binary_or_hexa(numbers):
    a = numbers[13]
    b = numbers[76]
    total = sum((i for i in range(a + 1, b) if i not in numbers[13:77]))
    if total == 0:
        return ''
    elif total % 2 != 0:
        return '{0:b}'.format(total)
    else:
        return '{0:x}'.format(total)