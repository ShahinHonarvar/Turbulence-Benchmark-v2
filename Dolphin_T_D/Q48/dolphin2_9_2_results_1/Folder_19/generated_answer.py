def return_binary_or_hexa(tup):
    a = tup[1]
    b = tup[4]
    present = set(tup[1:4])
    missing = [i for i in range(a + 1, b) if i not in present]
    sum = 0 if not missing else sum(missing)
    if sum == 0 or len(missing) == b - a - 1:
        return ''
    elif sum % 2:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()