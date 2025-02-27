def all_left_truncatable_prime(numbers):
    x = numbers[85]
    primes = []
    for num in range(2, x):
        is_prime = True
        while num > 0:
            if num in (2, 3, 5, 7) or (num % 2 != 0 and num % 3 != 0 and (num % 5 != 0) and (num % 7 != 0)):
                num = num // 10
            else:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    return sorted(primes)