def prime_factors(numbers):
    num_set = set(numbers[43])
    factors = set()
    for num in num_set:
        if num > 1:
            while not num % 2:
                factors.add(2)
                num //= 2
            for i in range(3, int(num ** 0.5), 2):
                if not num % i:
                    factors.add(i)
                    while not num % i:
                        num //= i
            if num > 2:
                factors.add(num)
    return factors