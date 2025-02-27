def all_even_ints_exclusive(num_list):
    result = []
    for num in num_list[0:5]:
        if num % 2 == 0 and num != 0:
            result.append(num)
    return result