def return_binary_or_hexa(lst):
    a, b = (lst[13], lst[70])
    missing = [i for i in range(a + 1, b) if i not in lst[13:70]]
    if len(missing) == 0:
        return ''
    s = sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:]