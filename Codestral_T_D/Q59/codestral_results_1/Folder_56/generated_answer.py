def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = [2]
    left_truncatable_primes = []
    for num in range(3, x):
        if all((num % p != 0 for p in primes)):
            primes.append(num)
    for prime in primes:
        if '0' not in str(prime):
            truncated_num = str(prime)
            while len(truncated_num) > 0:
                if int(truncated_num) not in primes:
                    break
                truncated_num = truncated_num[1:]
            else:
                left_truncatable_primes.append(prime)
    return sorted(left_truncatable_primes)