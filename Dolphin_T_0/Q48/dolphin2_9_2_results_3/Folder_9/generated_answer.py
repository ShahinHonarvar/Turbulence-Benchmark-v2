def return_binary_or_hexa(lst):
    a, b = (lst[70], lst[200])
    lst_range = [i + 1 for i in range(a, b)]
    missing = [val for val in lst if val not in lst_range]
    s = sum(lst_range) - sum(missing)
    if s % 2 == 1:
        return bin(s)[2:]
    else:
        return hex(s)[2:].upper()