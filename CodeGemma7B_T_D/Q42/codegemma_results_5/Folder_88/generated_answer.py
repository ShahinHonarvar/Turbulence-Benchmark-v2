def prime_factors(int_list):
    prime_factors = set()
    int_at_46 = int_list[46]
    for i in range(2, int(int_at_46 ** 0.5) + 1):
        if int_at_46 % i == 0:
            prime_factors.add(i)
            while int_at_46 % i == 0:
                int_at_46 //= i
    if int_at_46 > 1:
        prime_factors.add(int_at_46)
    return prime_factors