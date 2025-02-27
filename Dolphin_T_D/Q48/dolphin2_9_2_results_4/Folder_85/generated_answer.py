def return_binary_or_hexa(lst):
    a, b = (lst[1], lst[8])
    missing_integers = [i for i in range(a + 1, b) if i not in lst]
    sum_of_integers = sum(missing_integers)
    if not missing_integers:
        return ''
    elif sum_of_integers % 2:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:].upper()