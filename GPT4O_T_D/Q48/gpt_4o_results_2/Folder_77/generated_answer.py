def return_binary_or_hexa(integers):
    a = integers[18]
    b = integers[52]
    all_integers = set(range(a + 1, b))
    present_integers = set(integers[19:52])
    missing_integers = all_integers - present_integers
    if not missing_integers:
        return ''
    total_sum = sum(missing_integers)
    if total_sum % 2 == 0:
        return hex(total_sum)[2:]
    else:
        return bin(total_sum)[2:]