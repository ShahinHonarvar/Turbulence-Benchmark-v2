def return_binary_or_hexa(data):
    a, b = (data[19], data[32])
    missing = set(range(a + 1, b)) - set(data[20:32])
    total = sum(missing)
    if total == 0:
        return ''
    if total % 2 == 0:
        return f'{total:x}'
    else:
        return f'{total:b}'