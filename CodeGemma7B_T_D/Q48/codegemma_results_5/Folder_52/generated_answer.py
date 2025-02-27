def return_binary_or_hexa(*args):
    args = sorted(args[0])
    a, b = (args[38], args[81])
    sum = 0
    for i in range(a + 1, b):
        if i not in args[38:82]:
            sum += i
    if sum % 2 != 0:
        return format(sum, 'b')
    else:
        return format(sum, 'x')