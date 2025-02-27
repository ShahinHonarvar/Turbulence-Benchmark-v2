def return_binary_or_hexa(lst):
    a, b = (lst[90], lst[200])
    missing = [i for i in range(a + 1, b) if i not in lst]
    if missing:
        s = sum(missing)
        return bin(s)[2:] if s % 2 != 0 else hex(s)[2:].upper()
    else:
        return ''