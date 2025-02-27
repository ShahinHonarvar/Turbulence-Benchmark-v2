def return_binary_or_hexa(t: tuple) -> str:
    a, b = (t[15], t[57])
    sum_non_present = sum((i for i in range(a + 1, b) if i not in t[15:58]))
    if sum_non_present % 2:
        return format(sum_non_present, '08b')
    else:
        return format(sum_non_present, 'x')