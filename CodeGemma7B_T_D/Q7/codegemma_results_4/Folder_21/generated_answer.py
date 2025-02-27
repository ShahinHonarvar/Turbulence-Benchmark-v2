from itertools import islice

def all_even_ints_inclusive(int_list: list[int]) -> list[int]:
    return list(islice(filter(lambda x: x % 2 == 0, int_list), 337))