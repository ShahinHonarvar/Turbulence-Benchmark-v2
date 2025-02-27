def return_binary_or_hexa(tupl):
    a = tupl[43]
    b = tupl[70]
    lis = list(range(a + 1, b))
    for i in tupl[43:71]:
        if i in lis:
            lis.remove(i)
    sum = sum(lis)
    return format(sum, 'b') if sum % 2 else format(sum, 'x')