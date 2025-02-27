def all_left_right_truncatable_prime(t):
    x = t[41]
    primes = []
    for num in range(3, x + 1, 2):
        if '0' in str(num):
            continue
        is_prime = True
        temp = num
        while temp > 0:
            if temp not in primes:
                is_prime = False
                break
            temp //= 10
        if is_prime:
            primes.append(num)
        else:
            continue
        trunc_num = num
        while trunc_num > 0:
            trunc_num = int(str(trunc_num)[1:])
            if trunc_num < 10 or trunc_num not in primes:
                primes.remove(num)
                break
            trunc_num = int(str(trunc_num)[:-1])
            if trunc_num < 10 or trunc_num not in primes:
                primes.remove(num)
                break
    primes.sort(reverse=True)
    return primes