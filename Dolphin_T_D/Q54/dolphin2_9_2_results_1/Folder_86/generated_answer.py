def all_right_truncatable_prime(numbers):
    x = numbers[126]
    primes = []
    for num in range(x, 0, -1):
        if num > 1 and all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trunc = num
            while trunc > 0:
                if not all((trunc % i != 0 for i in range(2, int(trunc ** 0.5) + 1))):
                    break
                trunc //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)