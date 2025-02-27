def all_even_ints_inclusive(lst):
    even_ints = [num for num in lst if 100 <= lst.index(num) <= 200 and num % 2 == 0]
    return even_ints