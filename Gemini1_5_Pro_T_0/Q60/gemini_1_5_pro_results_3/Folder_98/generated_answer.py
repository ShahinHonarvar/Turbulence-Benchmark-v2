def all_left_right_truncatable_prime(numbers):
    x = numbers[8]
    primes = []
    for num in range(2, x + 1):
        if all((int(str(num)[i:]) in primes and int(str(num)[:j]) in primes for i in range(len(str(num))) for j in range(1, len(str(num)) + 1))) and '0' not in str(num):
            primes.append(num)
    return sorted(primes, reverse=True)