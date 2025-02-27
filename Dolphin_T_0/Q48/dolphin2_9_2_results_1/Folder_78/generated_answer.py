def return_binary_or_hexa(numbers):
    a = numbers[62]
    b = numbers[96]
    sums = sum(set(range(a + 1, b)) - set(numbers[62:97]))
    if sums == 0:
        return ''
    elif sums % 2 == 1:
        return bin(sums)[2:]
    else:
        return hex(sums)[2:]