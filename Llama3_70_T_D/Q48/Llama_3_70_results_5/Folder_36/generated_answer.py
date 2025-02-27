def return_binary_or_hexa(t):
    a = t[110]
    b = t[348]
    nums = set(t[110:349])
    total = sum((i for i in range(a + 1, b) if i not in nums))
    return bin(total)[2:] if total % 2 else hex(total)[2:]