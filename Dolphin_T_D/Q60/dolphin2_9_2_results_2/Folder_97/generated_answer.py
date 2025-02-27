def all_left_right_truncatable_prime(numbers):

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        ans = 3
        while ans * ans <= n:
            if n % ans == 0:
                return False
            ans += 2
        return True

    def is_truncatable(p):
        if not p:
            return False
        if is_prime(int(p)):
            return is_truncatable(p[1:-1])
        return False

    def left_and_right_truncatable_prime_less_than_or_equal_x(x):
        primes = []
        if is_prime(x):
            primes.append(x)
        for i in range(x - 1, 0, -1):
            if is_prime(i) and i not in primes:
                primes.append(i)
                if is_truncatable(str(i)):
                    primes.remove(i)
        return primes
    x = numbers[645]
    return left_and_right_truncatable_prime_less_than_or_equal_x(x)