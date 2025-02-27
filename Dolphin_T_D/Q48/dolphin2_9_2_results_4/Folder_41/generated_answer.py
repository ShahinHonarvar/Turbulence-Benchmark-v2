def return_binary_or_hexa(t):
    a = t[3]
    b = t[8]
    included = [i for i in t if 0 <= i <= b and i >= a]
    allowed_range = set(range(a + 1, b))
    not_included = allowed_range.difference(included)
    result = sum(not_included)
    if result % 2 == 0:
        return hex(result)[2:].upper()
    else:
        return bin(result)[2:]