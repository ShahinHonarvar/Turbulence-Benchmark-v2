def all_even_ints_exclusive(num_list):
    result = []
    for num in num_list[20:93]:
        if num % 2 == 0:
            result.append(num)
    return result if result else []