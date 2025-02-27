def return_binary_or_hexa(tup):
    a, b = (tup[36], tup[54])
    total = 0
    for num in range(a + 1, b):
        if num not in tup[36:55]:
            total += num
    return format(total, 'b') if total % 2 else format(total, 'x')