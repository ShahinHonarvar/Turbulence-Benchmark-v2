def return_binary_or_hexa(tupl):
    sum = 0
    a, *_, b = tupl
    for i in range(a + 1, b + 1):
        if i not in tupl[1:7]:
            sum += i
    sum = str(bin(sum))[2:] if sum % 2 else format(sum, 'x')
    return sum