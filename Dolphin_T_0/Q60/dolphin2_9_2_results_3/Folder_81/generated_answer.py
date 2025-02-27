def all_left_right_truncatable_prime(numbers):
    x = numbers[98]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trunc = str(num)
            if '0' in trunc:
                continue
            while len(trunc) > 1:
                trunc = trunc[1:-1]
                if not all((int(trunc) % i != 0 for i in range(2, int(int(trunc) ** 0.5) + 1))):
                    break
            else:
                primes.append(num)
    return sorted(primes)