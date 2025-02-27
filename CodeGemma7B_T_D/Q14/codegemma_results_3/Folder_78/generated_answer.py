from functools import partial
        from itertools import islice

def find_second_smallest_num(numbers):
    return next(islice(sorted((n for n in numbers[17:79] if isinstance(n, int)), key=int), 1), None)