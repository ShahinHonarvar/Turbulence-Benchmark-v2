def all_left_right_truncatable_prime(numbers):
    primes = [2, 3, 5, 7]
    x = numbers[89]
    for i in range(10, x + 1):
        if all((i % p != 0 for p in primes)):
            primes.append(i)
    left_right_truncatable_primes = [p for p in primes if str(p).count('0') == 0]
    for p in left_right_truncatable_primes[:]:
        if p < 10 or not (p // 10 in primes or p % 10 in primes):
            left_right_truncatable_primes.remove(p)
    return left_right_truncatable_primes[::-1]