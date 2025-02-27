def all_left_truncatable_prime(numbers):
    x = numbers[10]

    def is_left_truncatable_prime(n):
        if n < 10 and n in (2, 3, 5, 7):
            return True
        if '0' in str(n) or any([int(str(n)[i:]) not in (2, 3, 5, 7) and (not sympy.isprime(int(str(n)[i:]))) for i in range(len(str(n)))]):
            return False
        return True
    ltp = []
    for i in range(2, x):
        if is_left_truncatable_prime(i):
            ltp.append(i)
    ltp.sort(reverse=True)
    return ltp