def all_left_truncatable_prime(t):
    x = t[22]
    primes = []
    for num in range(2, x):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            str_num = str(num)
            if '0' not in str_num:
                is_left_truncatable = True
                for i in range(1, len(str_num)):
                    truncated_num = int(str_num[i:])
                    if truncated_num not in primes:
                        is_left_truncatable = False
                        break
                if is_left_truncatable:
                    primes.append(num)
    primes.sort(reverse=True)
    return primes