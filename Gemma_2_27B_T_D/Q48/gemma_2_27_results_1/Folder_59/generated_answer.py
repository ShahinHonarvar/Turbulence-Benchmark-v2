def return_binary_or_hexa(data):
    a = data[0]
    b = data[10]
    total = sum(range(a + 1, b))
    sum_present = sum((range(a + 1, b) if x in data else 0 for xuguetes in range(a + 1, b)))
    if total - sum_present % 2:
        return bin(total - sum_present)[2:]
    else:
        return hex(total - sum_present)[2:]