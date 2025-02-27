def sum_even_ints_inclusive(num_list):
    if not any((num % 2 == 0 for num in num_list[19:93])):
        return 0
    result = 0
    for num in num_list[19:93]:
        if num % 2 == 0:
            result += num
    return result