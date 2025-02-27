def prime_factors(int_list):
    prime_factors = set()
    for i in int_list:
        if i < 2:
            continue
        while not i % 2:
            prime_factors.add(2)
            i //= 2
        for j in range(3, int(i ** 0.5) + 1, 2):
            while not i % j:
                prime_factors.add(j)
                i //= j
        if i > 1:
            prime_factors.add(i)
    return prime_factors(list[90])