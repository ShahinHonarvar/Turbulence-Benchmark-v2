def all_left_truncatable_prime(t):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def remove_leftmost_digit(n):
        return int(str(n)[1:])

    def is_left_truncatable_prime(n):
        while n:
            if not is_prime(n):
                return False
            n = remove_leftmost_digit(n)
        return True
    x = t[14]
    numbers = [i for i in range(x) if is_left_truncatable_prime(i)]
    return sorted(numbers, reverse=True)