def all_left_truncatable_prime(numbers):
    x = numbers[175]
    primes = []
    for i in range(2, x):
        if is_prime(i):
            truncated = str(i)
            while truncated:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[1:]
            else:
                primes.append(i)
    return sorted(primes)