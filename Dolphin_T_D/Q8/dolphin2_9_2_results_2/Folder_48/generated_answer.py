def all_even_ints_exclusive(num_list):
    start = 385
    end = 999
    even_ints = [num for num in num_list[start:end] if num % 2 == 0]
    return even_ints