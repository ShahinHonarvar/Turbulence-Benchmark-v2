def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[77]
    b = tuple_of_integers[84]
    numbers_between_a_and_b = set(range(a + 1, b))
    included_numbers = set(tuple_of_integers[78:84])
    if numbers_between_a_and_b.issubset(included_numbers):
        return ''
    gap_numbers = numbers_between_a_and_b.difference(included_numbers)
    sum_of_gap_numbers = sum(gap_numbers)
    if sum_of_gap_numbers % 2 != 0:
        return bin(sum_of_gap_numbers)[2:]
    else:
        return hex(sum_of_gap_numbers)[2:]