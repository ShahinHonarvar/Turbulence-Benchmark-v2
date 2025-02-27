def prime_factors(num_list):
    prime_factors_set = set()
    num = num_list[38]
    for i in range(2, num + 1):
        if num % i == 0:
            while num % i == 0:
                prime_factors_set.add(i)
                num = num // i
    return prime_factors_set