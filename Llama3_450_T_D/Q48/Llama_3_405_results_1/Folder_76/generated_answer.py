def return_binary_or_hexa(tup):
    if len(tup) <= 905:
        return ''
    a = tup[450]
    b = tup[905]
    total = sum(range(a + 1, b))
    present = sum((num for num in tup[451:905] if a < num < b))
    diff = total - present
    if diff == 0:
        return ''
    if diff % 2 != 0:
        return bin(diff)[2:]
    return hex(diff)[2:]