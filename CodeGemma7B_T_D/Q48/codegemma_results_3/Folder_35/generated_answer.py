def return_binary_or_hexa(numbers):
    a = numbers[76]
    b = numbers[83]
    the_sum = sum((n for n in range(a + 1, b) if n not in numbers[77:84]))
    if the_sum % 2 == 1:
        return str(bin(the_sum))[2:]
    else:
        return str(hex(the_sum))[2:].upper()