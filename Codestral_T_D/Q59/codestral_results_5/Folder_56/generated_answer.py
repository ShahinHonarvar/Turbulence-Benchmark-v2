def all_left_truncatable_prime(numbers):
    x = numbers[30]
    primes = []
    for i in range(2, x):
        if all((i % j != 0 for j in range(2, int(i ** 0.5) + 1))) and '0' not in str(i):
            num = i
            while num:
                num = num // 10
                if num > 0 and (not all((num % j != 0 for j in range(2, int(num ** 0.5) + 1)))):
                    break
            else:
                primes.append(i)
    return sorted(primes)