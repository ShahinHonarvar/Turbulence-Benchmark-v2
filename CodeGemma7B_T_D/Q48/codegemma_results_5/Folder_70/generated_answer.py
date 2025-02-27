def return_binary_or_hexa(tup):
    a = tup[43]
    b = tup[70]
    nums = set(tup)
    sum = 0
    for i in range(a + 1, b):
        if i not in nums:
            sum += i
    if sum % 2 == 1:
        return bin(sum)[2:]
    else:
        return hex(sum)[2:].upper()