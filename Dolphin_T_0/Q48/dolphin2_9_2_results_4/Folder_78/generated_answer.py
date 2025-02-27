def return_binary_or_hexa(integers):
    a = integers[62]
    b = integers[96]
    missing_integers = [x for x in range(a + 1, b) if x not in integers]
    if not missing_integers:
        return ''
    sum_missing_integers = sum(missing_integers)
    if sum_missing_integers % 2 == 0:
        return hex(sum_missing_integers)[2:]
    return bin(sum_missing_integers)[2:]