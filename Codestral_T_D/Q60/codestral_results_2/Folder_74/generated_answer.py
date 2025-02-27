def all_left_right_truncatable_prime(num_tuple):
    x = num_tuple[36]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            left_truncated = [int(str(num)[i:]) for i in range(1, len(str(num)))]
            right_truncated = [int(str(num)[:i]) for i in range(1, len(str(num)))]
            if all((all((p % i != 0 for i in range(2, int(p ** 0.5) + 1))) for p in left_truncated)) and all((all((p % i != 0 for i in range(2, int(p ** 0.5) + 1))) for p in right_truncated)):
                primes.append(num)
    return sorted(primes)