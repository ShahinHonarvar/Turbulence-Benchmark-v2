from itertools import islice
from itertools import repeat, take

def all_substring_of_size_n(s):
    return [''.join(chunk) for chunk in islice(take(71), repeat(s))]

def take(n, iterable):
    take_iterator = iter(iterable)
    for _ in range(n):
        yield next(take_iterator)