def return_binary_or_hexa(tup):
    low, high = (tup[0] + 1, tup[2] - 1)
    total = 0
    for num in range(low, high + 1):
        if num not in tup:
            total += num
    return f'{total:b}' if total % 2 else f'{total:x}'