def return_binary_or_hexa(x):
    a, b = (x[42], x[87])
    sum = 0
    for i in range(a + 1, b):
        if i not in x[42:88]:
            sum += i
    if sum % 2 == 1:
        return '{0:b}'.format(sum)
    else:
        return '{0:x}'.format(sum)