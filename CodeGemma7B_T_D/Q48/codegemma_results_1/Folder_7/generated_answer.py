def return_binary_or_hexa(*args):
    tup, a, b = (args[0], args[10], args[97])
    sum = 0
    for num in range(a + 1, b):
        if num not in tup[a:b]:
            sum += num
    if sum % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].upper()