def all_even_ints_exclusive(integer_list):
    even_list = [integer for integer in integer_list[1:-1] if integer % 2 == 0]
    return even_list