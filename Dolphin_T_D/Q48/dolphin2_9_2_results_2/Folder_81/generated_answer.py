def return_binary_or_hexa(integers):
    a = integers[10]
    b = integers[100]
    all_integers = set(range(a + 1, b))
    subset = set(integers[11:100])
    missing_integers = all_integers - subset
    sum_missing = sum(missing_integers)
    if sum_missing % 2 == 1:
        return bin(sum_missing)[2:]
    else:
        return hex(sum_missing)[2:].upper()