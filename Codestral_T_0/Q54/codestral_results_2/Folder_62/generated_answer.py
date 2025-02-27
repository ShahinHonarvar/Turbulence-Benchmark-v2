def all_right_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            truncated_num = num
            while truncated_num > 0:
                if truncated_num not in primes:
                    break
                truncated_num //= 10
            else:
                primes.append(num)
    return sorted(primes)