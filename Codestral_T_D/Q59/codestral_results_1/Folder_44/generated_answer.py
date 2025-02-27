def all_left_truncatable_prime(t):
    x = t[39]
    primes = []
    for num in range(2, x):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))) and '0' not in str(num):
            truncated_num = str(num)
            while truncated_num:
                if int(truncated_num) not in primes:
                    break
                truncated_num = truncated_num[1:]
            else:
                primes.append(num)
    return sorted(primes)