def all_even_ints_exclusive(lst):
    start = 80
    end = 200
    return [n for n in lst[start:end] if n % 2 == 0]