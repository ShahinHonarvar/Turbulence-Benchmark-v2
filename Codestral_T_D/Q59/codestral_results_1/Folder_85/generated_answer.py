def all_left_truncatable_prime(numbers):
    x = numbers[94]
    primes = []
    for num in range(2, x):
        if all((int(num[i:]) in primes for i in range(1, len(num)))) and int(num) in primes:
            primes.append(int(num))
        elif '0' not in num and all((int(num[i:]) in primes for i in range(1, len(num)))):
            primes.append(int(num))
    return sorted(primes)