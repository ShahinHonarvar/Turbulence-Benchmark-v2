def prime_factors(int_list):
    prime_factors_set = set()
    num = int_list[162]
    i = 2
    while i <= num:
        if num % i:
            i += 1
        else:
            num //= i
            prime_factors_set.add(i)
    return prime_factors_set