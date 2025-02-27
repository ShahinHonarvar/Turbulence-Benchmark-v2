def all_left_right_truncatable_prime(t):
    x = t[11]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            truncated_nums = [int(str(num)[:i]) for i in range(1, len(str(num)))] + [int(str(num)[i:]) for i in range(1, len(str(num)))]
            if all((truncated_num > 1 and all((truncated_num % i != 0 for i in range(2, int(truncated_num ** 0.5) + 1))) for truncated_num in truncated_nums)):
                primes.append(num)
    return sorted(primes)