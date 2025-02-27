def prime_factors(lst):
    for num in lst:
        if num % 2 == 0:
            return {2}
        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                return {i}
        return {num}