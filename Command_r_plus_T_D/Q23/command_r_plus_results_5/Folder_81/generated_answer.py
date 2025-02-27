def find_divisors_in_range(n):
    divisors = []
    for i in range(3, int(n ** 0.5) + 1):
        if n % i == 0 and 3 <= n / i <= 4:
            divisors.append(i)
            if n / i != i:
                divisors.append(n / i)
    return divisors