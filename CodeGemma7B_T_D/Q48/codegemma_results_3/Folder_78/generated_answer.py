def return_binary_or_hexa(num_tuple):
    a = num_tuple[62]
    b = num_tuple[96]
    total = 0
    for i in range(a + 1, b):
        if i not in num_tuple[62:97]:
            total += i
    return format(total, '#b') if total % 2 else format(total, '#x')