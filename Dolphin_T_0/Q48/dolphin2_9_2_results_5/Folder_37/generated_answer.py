def return_binary_or_hexa(lst):
    a, b = (lst[2], lst[7])
    missing = [i for i in range(a + 1, b) if i not in lst]
    s = sum(missing)
    if s:
        return bin(s)[2:] if s % 2 else hex(s)[2:].lower()
    return ''