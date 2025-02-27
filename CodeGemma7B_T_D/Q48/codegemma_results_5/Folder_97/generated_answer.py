def return_binary_or_hexa(tuple):
    if len(tuple) < 103:
        return None
    a = tuple[34] + 1
    b = tuple[69] - 1
    sum = 0
    for i in range(a, b + 1):
        if i not in tuple:
            sum += i
    if sum % 2 == 0:
        hex = ''.join(format(sum // 16, 'X'), format(sum % 16, 'X'))
        return hex
    else:
        binary = ''
        while sum != 0:
            binary = str(sum % 2) + binary
            sum //= 2
        return binary