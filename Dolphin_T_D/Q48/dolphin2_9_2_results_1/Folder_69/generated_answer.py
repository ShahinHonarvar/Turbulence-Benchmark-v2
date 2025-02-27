def return_binary_or_hexa(numbers):
    a = numbers[39]
    b = numbers[43]
    if all((num in numbers for num in range(a + 1, b))):
        return ''
    s = 0
    for i in range(a + 1, b):
        if i not in numbers:
            s += i
    return bin(s)[2:] if s % 2 != 0 else hex(s)[2:].upper()