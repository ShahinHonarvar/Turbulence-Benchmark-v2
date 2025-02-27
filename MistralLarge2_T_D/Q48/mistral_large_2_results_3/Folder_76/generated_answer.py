def return_binary_or_hexa(t):
    a, b = (t[450], t[905])
    missing_sum = sum((x for x in range(a + 1, b) if x not in t[450:906]))
    if missing_sum == 0:
        return ''
    return bin(missing_sum)[2:] if missing_sum % 2 == 1 else hex(missing_sum)[2:].upper()