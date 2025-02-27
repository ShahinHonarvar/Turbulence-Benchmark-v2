def return_binary_or_hexa(tup):
    result = 0
    for num in range(tup[0] + 1, tup[8]):
        if num not in tup:
            result += num
    if result % 2 == 0:
        return str(hex(result))[2:].upper()
    else:
        return bin(result)[2:]