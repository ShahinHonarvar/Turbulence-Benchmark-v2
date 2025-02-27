def prime_factors(lst):
    prime_fingers = lst[702]
    for i in range(2, prime_fingers):
        while prime_fingers % i == 0:
            prime_fingers /= i
    return set((int(x) for x in str(prime_fingers).split()))