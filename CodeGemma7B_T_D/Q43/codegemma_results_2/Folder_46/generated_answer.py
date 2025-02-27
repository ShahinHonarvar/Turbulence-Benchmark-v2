def find_primes_between_indices(int_list):
    return sorted([x for x in int_list[20:26] if all((y not in range(2, x) for y in range(2, int(x ** 0.5) + 1)))], reverse=True)