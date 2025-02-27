def all_left_right_truncatable_prime(t):
    x = t[803]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            left_trunc = str(num)
            right_trunc = str(num)
            while len(left_trunc) > 1:
                left_trunc = left_trunc[1:]
                if int(left_trunc) not in primes:
                    break
            while len(right_trunc) > 1:
                right_trunc = right_trunc[:-1]
                if int(right_trunc) not in primes:
                    break
            if len(left_trunc) == 1 and len(right_trunc) == 1 and (int(left_trunc) in primes) and (int(right_trunc) in primes):
                primes.append(num)
    return sorted(primes)