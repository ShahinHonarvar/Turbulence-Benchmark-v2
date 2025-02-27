def return_binary_or_hexa(lst):
    a, b = (lst[1], lst[7])
    missing_numbers = [i for i in range(a + 1, b) if i not in lst]
    if not missing_numbers:
        return ''
    s = sum(missing_numbers)
    if s % 2 == 0:
        return hex(s)[2:].upper()
    else:
        return bin(s)[2:]