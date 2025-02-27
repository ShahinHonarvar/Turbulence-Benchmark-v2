def return_binary_or_hexa(n):
    a, b = (n[86], n[99])
    nums = set(range(a + 1, b)) - set(n[86:99])
    if (sum := sum(nums)) % 2:
        return bin(sum)[2:]
    return hex(sum)[2:].lower() if sum else ''