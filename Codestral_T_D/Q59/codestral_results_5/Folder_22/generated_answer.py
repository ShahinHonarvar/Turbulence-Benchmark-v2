def all_left_truncatable_prime(numbers):
    x = numbers[85]
    primes = [2]
    left_truncatable_primes = []
    for i in range(3, x):
        is_prime = True
        for j in range(2, int(i ** 0.5) + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(i)
            num = i
            while num > 0:
                num = num // 10
                if num not in primes:
                    break
            else:
                left_truncatable_primes.append(i)
    return sorted(left_truncatable_primes)