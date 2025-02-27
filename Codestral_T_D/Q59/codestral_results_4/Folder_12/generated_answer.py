def all_left_truncatable_prime(numbers):
    x = numbers[70]
    primes = []
    for num in range(2, x):
        if all((int(num[i:]) in primes for i in range(1, len(num)))) and '0' not in num:
            primes.append(int(num))
    return sorted(primes, reverse=True)