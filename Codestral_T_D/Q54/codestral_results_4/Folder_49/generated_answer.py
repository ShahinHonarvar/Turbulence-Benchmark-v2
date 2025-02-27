def all_right_truncatable_prime(numbers):
    x = numbers[14]
    right_truncatable_primes = []
    for n in range(2, x):
        is_prime = True
        num = n
        while num > 0:
            if num < 2 or any((num % i == 0 for i in range(2, int(num ** 0.5) + 1))):
                is_prime = False
                break
            num //= 10
        if is_prime:
            right_truncatable_primes.append(n)
    return sorted(right_truncatable_primes)