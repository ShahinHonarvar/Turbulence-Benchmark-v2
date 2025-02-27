def all_right_truncatable_prime(t):
    x = t[78]
    primes = [2, 3, 5, 7]
    for num in range(11, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            trunc_num = num
            while trunc_num > 0:
                if trunc_num not in primes:
                    break
                trunc_num //= 10
            else:
                primes.append(num)
    return sorted(primes, reverse=True)