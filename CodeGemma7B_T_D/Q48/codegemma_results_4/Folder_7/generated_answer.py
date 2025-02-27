def return_binary_or_hexa(t):
    a, b = (t[97], t[10])
    sum = 0
    for i in range(a + 1, b):
        if i not in t[10:98]:
            sum += i
    return f'{sum:b}' if sum % 2 else f'{sum:x}'