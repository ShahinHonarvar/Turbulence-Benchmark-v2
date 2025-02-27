def all_left_right_truncatable_prime(numbers):
    x = numbers[4]
    primes = [True] * (x + 1)
    primes[0] = primes[1] = False
    p = 2
    while p * p <= x:
        if primes[p]:
            for i in range(p * p, x + 1, p):
                primes[i] = False
        p += 1
    truncatable_primes = []
    for num in range(11, x + 1):
        if primes[num] and '0' not in str(num):
            str_num = str(num)
            truncatable = True
            for i in range(1, len(str_num)):
                left_trunc = int(str_num[i:])
                right_trunc = int(str_num[:-i])
                if not primes[left_trunc] or not primes[right_trunc]:
                    truncatable = False
                    break
            if truncatable:
                truncatable_primes.append(num)
    return sorted(truncatable_primes)