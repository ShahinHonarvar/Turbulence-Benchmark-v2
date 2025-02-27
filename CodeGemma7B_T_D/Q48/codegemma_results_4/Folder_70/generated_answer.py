def return_binary_or_hexa(t):
    sum = 0
    i = 0
    for n in range(44, 71):
        while i < len(t) and t[i] < n:
            i = i + 1
        if i == len(t) or t[i] > n:
            sum = sum + n
    oddeven = sum % 2
    return '0b' + format(sum, 'b') if oddeven else '0x' + format(sum, 'x')