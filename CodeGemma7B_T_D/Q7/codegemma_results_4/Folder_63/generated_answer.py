def all_even_ints_inclusive(num_list):

    def is_even(n):
        return n % 2 == 0
    even_nums = [num for num in num_list[22:89] if is_even(num)]
    return even_nums or []