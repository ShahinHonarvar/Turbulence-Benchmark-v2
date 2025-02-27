def all_left_right_truncatable_prime(t):
    x = t[20]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            truncated_nums = [int(str(num)[:i]) for i in range(1, len(str(num)))] + [int(str(num)[i:]) for i in range(1, len(str(num)))]
            if all((all((trunc % i != 0 for i in range(2, int(trunc ** 0.5) + 1))) for trunc in truncated_nums)):
                primes.append(num)
    return sorted(primes, reverse=True)