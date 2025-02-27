def return_binary_or_hexa(t):
    seventeen = t[77] + 1
    ninetytwo = t[84] - 1
    present = set(t[77:85])
    sum = 0
    for i in range(seventeen, ninetythree):
        if i not in present:
            sum += i
    if sum % 2 == 1:
        return format(sum, 'b')
    else:
        return format(sum, 'x')