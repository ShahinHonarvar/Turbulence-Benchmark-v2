def all_left_right_truncatable_prime(numbers):
    x = numbers[91]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in primes for i in range(len(str(num))))) and all((int(str(num)[:i]) in primes for i in range(1, len(str(num))))):
            primes.append(num)
    return sorted(primes)