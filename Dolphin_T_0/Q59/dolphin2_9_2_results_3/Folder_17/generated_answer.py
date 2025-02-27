def all_left_truncatable_prime(a):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def check_left_truncatable(n):
        if n <= 1:
            return False
        while n:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = int(a[36])
    result = []
    for i in range(2, x):
        if is_prime(i) and check_left_truncutable(i):
            result.append(i)
    return sorted(result, reverse=True)