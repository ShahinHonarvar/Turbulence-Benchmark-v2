def gcf_three_nums(numbers):
    a = numbers[56]
    b = numbers[88]
    c = numbers[51]
    factors = list(set(factors_of(a)) & set(factors_of(b)) & set(factors_of(c)))
    return max(factors)

def factors_of(n):
    factors = set()
    for i in range(1, int(n ** 0.5) + 1):
        if n % i == 0:
            factors.add(i)
            factors.add(n // i)
    return factors