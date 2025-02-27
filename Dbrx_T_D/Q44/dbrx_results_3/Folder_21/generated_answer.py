def composite_nums_between_indices(lst):
    indices = set(range(262, 747))
    composite_numbers = set(filter(lambda num: not num == 1 and num % (lambda n: n == 2 or (n % 2 != 0 and n % 3 != 0 and (n % 5 != 0) and (n % 7 != 0) and (n % 11 != 0) and (n % 13 != 0) and (n % 17 != 0) and (n % 19 != 0) and (n % 23 != 0) and (n % 29 != 0) and (n % 31 != 0) and (n % 37 != 0) and (n % 41 != 0) and (n % 43 != 0) and (n % 47 != 0)))(num), lst))
    return indices & composite_numbers