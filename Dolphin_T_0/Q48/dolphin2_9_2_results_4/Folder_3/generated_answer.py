def return_binary_or_hexa(t):
    a, b = (t[56], t[88])
    integers_between_a_b = set(range(a + 1, b))
    present_integers = set(t[57:88])
    missing_integers = integers_between_a_b - present_integers
    sum_of_missing_integers = sum(missing_integers)
    if not missing_integers:
        return ''
    elif sum_of_missing_integers % 2:
        return bin(sum_of_missing_integers)[2:]
    else:
        return hex(sum_of_missing_integers)[2:]