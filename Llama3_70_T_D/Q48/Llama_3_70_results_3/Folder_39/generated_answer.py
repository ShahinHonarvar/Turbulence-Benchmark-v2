def return_binary_or_hexa(tup):
    a = tup[44]
    b = tup[91]
    nums = set(tup[44:92])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total % 2:
        return bin(total)[2:]
    else:
        return hex(total)[2:]