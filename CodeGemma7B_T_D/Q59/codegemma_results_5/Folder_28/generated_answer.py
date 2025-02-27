def all_left_truncatable_prime(tp):
    x = tp[19]
    ans = set()
    for i in range(2, x):
        if isprime(i) and '0' not in str(i) and isprime(i + 1):
            n = i + 1
            while n < x and isprime(n):
                n += int(str(n)[:-1])
            if n < x:
                continue
            n = i
            while n < x and isprime(n):
                n += int(str(n)[1:])
            if n < x:
                continue
            ans.add(i)
    return sorted(list(ans))