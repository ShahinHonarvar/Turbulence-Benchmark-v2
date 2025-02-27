def all_right_truncatable_prime(numbers):
    x = numbers[175]
    primes = [2]
    for num in range(3, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            primes.append(num)
    truncatable_primes = []
    for prime in primes:
        last_digit = int(str(prime)[-1])
        truncated_num = int(str(prime)[:-1])
        while truncated_num != 0:
            if truncated_num not in primes:
                break
            last_digit = int(str(truncated_num)[-1])
            truncated_num = int(str(truncated_num)[:-1])
        else:
            truncatable_primes.append(prime)
    return sorted(truncatable_primes)