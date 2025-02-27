def all_right_truncatable_prime(numbers):
    x = numbers[50]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            truncated = str(num)
            while truncated:
                if int(truncated) not in primes:
                    break
                truncated = truncated[:-1]
            else:
                primes.append(num)
    return sorted(primes, reverse=True)