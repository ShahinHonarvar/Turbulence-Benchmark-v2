def all_left_right_truncatable_prime(x):

    def is_prime(n):
        if n <= 1 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def left_truncatable_prime(n):
        if not (n > 1 and all((digit != '0' for digit in str(n)))):
            return False
        return is_prime(n)

    def right_truncatable_prime(n):
        if not (n > 1 and all((digit != '0' for digit in str(n)))):
            return False
        while n >= 10:
            n //= 10
            if not is_prime(n):
                return False
        return True
    result = []
    for i in range(2, x + 1):
        if left_truncatable_prime(i) and right_truncatable_prime(i):
            result.append(i)
    return sorted(result)