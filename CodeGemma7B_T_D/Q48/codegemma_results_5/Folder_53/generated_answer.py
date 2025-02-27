def return_binary_or_hexa(tuples):
    ranges = list(range(tuples[200] + 1, tuples[202] + 1))
    missing_numbers_in_range = [x for x in ranges if x not in tuples]
    if not missing_numbers_in_range:
        return ''
    total_sum = sum(missing_numbers_in_range)
    if total_sum % 2 == 1:
        return '{:b}'.format(total_sum)
    else:
        return '{:x}'.format(total_sum).upper()