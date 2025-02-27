def return_binary_or_hexa(numbers):
    a = numbers[57]
    b = numbers[85]
    missing = [i for i in range(a + 1, b) if i not in numbers[58:85]]
    if not missing:
        return ''
    s = sum(missing)
    if s % 2 == 0:
        return string(hex(s), 16).lower()
    else:
        return bin(s)[2:]