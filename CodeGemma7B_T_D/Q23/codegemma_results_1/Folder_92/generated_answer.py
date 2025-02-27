def find_divisors_in_range(n):
    divisors = []
    for i in range(8, 10):
        if i ** 2 <= n:
            if n % i == 0:
                divisors.append(i)
                if n / i != i:
                    divisors.append(n // i)
    return divisors