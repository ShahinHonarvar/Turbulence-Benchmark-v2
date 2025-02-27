def return_binary_or_hexa(t):
    result = 0
    for i in range(t[0] + 1, t[10]):
        if i not in t:
            result += i
    if result & 1:
        return f'{result:b}'
    else:
        return f'{result:x}'