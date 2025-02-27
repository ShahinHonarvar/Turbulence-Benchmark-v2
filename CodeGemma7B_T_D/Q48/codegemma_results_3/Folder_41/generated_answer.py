def return_binary_or_hexa(t):
    a, b = (t[3], t[8])
    sum = 0
    for i in range(a + 1 if a >= 3 else 3, b):
        if t[i] not in t[3:8]:
            sum += i
    return f'{sum:b}' if sum % 2 else f'{sum:x}'