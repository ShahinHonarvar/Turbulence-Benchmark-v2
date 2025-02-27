def return_binary_or_hexa(tuple_of_integers):
    a = tuple_of_integers[0]
    b = tuple_of_integers[-1]
    numbers_range = list(range(a + 1, b))
    numbers_in_tuple = list(tuple_of_integers)
    Missing_numbers = [i for i in numbers_range if i not in numbers_in_tuple]
    if len(Missing_numbers) == 0:
        return ''
    sum_of_missing_numbers = sum(Missing_numbers)
    if sum_of_missing_numbers % 2 == 0:
        return hex(sum_of_missing_numbers)[2:].upper()
    else:
        return bin(sum_of_missing_numbers)[2:]