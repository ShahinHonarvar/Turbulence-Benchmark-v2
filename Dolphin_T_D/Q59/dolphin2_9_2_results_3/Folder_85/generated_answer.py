def all_left_truncatable_prime(t):
    x = t[94]
    primes = [2]
    for num in range(3, x):
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            primes.append(num)
    result = []
    for v in primes:
        m = v
        while m > 0:
            if m not in result:
                result.append(m)
            if m // 10 > 0 and m not in primes:
                break
            m = m // 10
    return sorted(list(set(result)))