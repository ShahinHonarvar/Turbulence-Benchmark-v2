def all_left_right_truncatable_prime(n):
    x = n[49]
    primes = [2, 3, 5, 7]
    for num in range(11, x + 1):
        if all((num % i != 0 for i in range(2, num))):
            primes.append(num)

    def is_truncatable_prime(n):
        for i in range(n, 0, -1):
            if int(str(n)[-i:]) in primes and int(str(n)[:-i]) in primes:
                continue
            else:
                return False
        return True
    return sorted([num for num in primes if is_truncatable_prime(num)])