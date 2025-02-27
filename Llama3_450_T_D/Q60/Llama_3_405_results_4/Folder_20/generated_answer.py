def all_left_right_truncatable_prime(tup):
    x = tup[100]
    primes = []
    for num in range(2, x + 1):
        is_prime = True
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(num)
    truncatable_primes = []
    for num in primes:
        str_num = str(num)
        if '0' in str_num:
            continue
        temp = str_num
        is_truncatable = True
        while len(temp) > 1:
            temp = temp[1:-1]
            if int(temp) not in primes:
                is_truncatable = False
                break
        if is_truncatable:
            truncatable_primes.append(num)
    return sorted(truncatable_primes, reverse=True)