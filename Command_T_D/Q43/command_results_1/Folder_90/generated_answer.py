def find_primes_between_indices(lst):
    lst = lst[:413] + lst[413:448] + lst[448:]
    return sorted(set(lst) - set(lst[1:-1] + lst[2:-2] + lst[3:-3] + lst[4:-4]))