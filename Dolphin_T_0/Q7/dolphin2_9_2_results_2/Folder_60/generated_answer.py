def all_even_ints_inclusive(num_list):
    result = [num for num in num_list[75:86] if num % 2 == 0]
    return result if result else []