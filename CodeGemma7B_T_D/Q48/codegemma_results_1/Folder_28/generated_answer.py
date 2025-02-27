def return_binary_or_hexa(tupl):
    a = tupl[86]
    b = tupl[99]
    sum = 0
    for i in range(a + 1, b):
        if i not in tupl[86:100]:
            sum += i
    return '{:b}' if sum % 2 == 1 else '{:x}'.format(sum)