def return_binary_or_hexa(t):
    a = t[44]
    b = t[78]
    missing = [x for x in range(a + 1, b) if x not in t[44:79]]
    the_sum = sum(missing)
    return bin(the_sum)[2:] if the_sum % 2 == 1 else hex(the_sum)[2:] if missing else ''