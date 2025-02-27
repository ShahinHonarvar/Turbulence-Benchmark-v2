def return_binary_or_hexa(lst):
    a, b = (lst[18], lst[52])
    present_in_lst = set(lst[19:52])
    sum_of_integers = sum([n for n in range(a + 1, b) if n not in present_in_lst])
    if sum_of_integers % 2 == 1:
        return bin(sum_of_integers)[2:]
    else:
        return hex(sum_of_integers)[2:]