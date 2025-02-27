def all_right_truncatable_prime(tuple_of_positive_integers):
    x = tuple_of_positive_integers[100]

    def is_prime(n):
        if n == 2 or n == 3:
            return True
        if n < 2 or n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_right_truncatable_prime(n):
        while n != 0:
            if not is_prime(n):
                return False
            n //= 10
        return True
    right_truncatables = []
    for i in range(2, x):
        if is_right_truncatable_prime(i):
            right_truncatables.append(i)
    return sorted(right_truncatables)