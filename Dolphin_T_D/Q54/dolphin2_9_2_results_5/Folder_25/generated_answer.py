def all_right_truncatable_prime(x):
    primes = [2]
    right = 0
    for num in range(3, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            while right > 0 and num // 10 ** right == num:
                right -= 1
            if right == 0:
                primes.append(num)
    right_truncatable_primes = []
    for prime in primes:
        copy_prime = prime
        while copy_prime > 1:
            if copy_prime in primes:
                right_truncatable_primes.append(copy_prime)
                copy_prime //= 10
            else:
                break
    return sorted(list(set(right_truncatable_primes)))