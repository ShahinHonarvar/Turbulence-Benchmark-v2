def return_binary_or_hexa(order):
    a = order[70]
    b = order[98]
    nums = set((i for i in range(a + 1, b + 1)))
    missing = nums - set(order[70:99])
    sum = sum(missing)
    return f'{sum:08b}' if sum % 2 else f'{sum:08x}'