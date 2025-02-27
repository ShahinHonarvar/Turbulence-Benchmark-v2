from collections import defaultdict

def prime_factors(num_list):
    prime_factors = defaultdict(set)
    for num in num_list:
        for factor in range(2, num + 1):
            while num % factor == 0:
                prime_factors[num].add(factor)
                num //= factor
    return prime_factors[num_list[53]]