def return_binary_or_hexa(tupl):
    a, b = (tupl[18], tupl[52])
    excludes = set(tupl[18:53])
    _sum = sum((i for i in range(a + 1, b) if i not in excludes))
    return bin(_sum)[2:] if _sum % 2 else hex(_sum)[2:].upper() if len(_sum) % 2 else hex(_sum)[2:]