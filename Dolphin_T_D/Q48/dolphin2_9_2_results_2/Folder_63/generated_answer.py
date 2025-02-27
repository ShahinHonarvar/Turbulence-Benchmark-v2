def return_binary_or_hexa(lst):
    a = lst[81]
    b = lst[86]
    missing = [x for x in range(a + 1, b) if x not in lst[81:86]]
    if not missing:
        return ''
    total = sum(missing)
    return bin(total).replace('0b', '') if total % 2 else hex(total).replace('0x', '')