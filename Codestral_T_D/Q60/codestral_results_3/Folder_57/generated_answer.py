def all_left_right_truncatable_prime(t):
    x = t[54]
    primes = []
    for num in range(2, x + 1):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            if '0' not in str_num:
                left_trunc = [int(str_num[i:]) for i in range(len(str_num))]
                right_trunc = [int(str_num[:i]) for i in range(1, len(str_num))]
                if all((all((j % i != 0 for i in range(2, int(j ** 0.5) + 1))) for j in left_trunc + right_trunc)):
                    primes.append(num)
    return sorted(primes, reverse=True)