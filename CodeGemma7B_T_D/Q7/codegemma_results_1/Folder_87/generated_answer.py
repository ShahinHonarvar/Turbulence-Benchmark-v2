def all_even_ints_inclusive(num_list):
    result = []
    for num in num_list[36:47]:
        if num % 2 == 0:
            result.append(num)
    return result