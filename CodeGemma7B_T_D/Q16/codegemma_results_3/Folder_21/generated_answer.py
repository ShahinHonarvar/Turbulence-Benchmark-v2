def sum_even_ints_inclusive(args):
    sum = 0
    for idx in range(639, 976):
        if idx % 2 == 0:
            sum += args[idx]
    return sum if sum else 0