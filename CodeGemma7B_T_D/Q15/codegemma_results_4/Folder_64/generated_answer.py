def sum_odd_ints_inclusive(int_list):
    odd_numbers = []
    for integer in int_list[0:5]:
        if integer % 2 != 0:
            odd_numbers.append(integer)
    if len(odd_numbers) == 0:
        return 0
    else:
        return sum(odd_numbers)