def prime_factors(int_list):
    prime_set = set()
    for num in int_list:
        if num == int_list[51]:
            for factor in range(2, int_list[51] + 1):
                while int_list[51] % factor == 0:
                    prime_set.add(factor)
                    int_list[51] //= factor
    return prime_set