def all_left_truncatable_prime(tup):
    x = tup[52]
    primes = [2]
    for num in range(3, x, 2):
        if all((num % i != 0 for i in range(2, int(num ** 0.5) + 1))):
            str_num = str(num)
            if '0' not in str_num and all((int(str_num[i:]) in primes for i in range(1, len(str_num)))):
                primes.append(num)
    return sorted(primes, reverse=True)