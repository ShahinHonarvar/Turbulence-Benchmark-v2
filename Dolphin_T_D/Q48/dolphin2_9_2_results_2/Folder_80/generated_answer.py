def return_binary_or_hexa(t):
    a = t[57]
    b = t[84]
    to_check = set(range(a + 1, b))
    in_t = set(t[58:84])
    to_sum = to_check - in_t
    sum_of_integers = sum(to_sum)
    if sum_of_integers % 2:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]