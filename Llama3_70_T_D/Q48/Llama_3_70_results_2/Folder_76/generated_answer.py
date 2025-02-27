def return_binary_or_hexa(tup):
    a = tup[450]
    b = tup[905]
    nums = set(tup[450:906])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    if total % 2 != 0:
        return bin(total)[2:]
    else:
        return hex(total)[2:]