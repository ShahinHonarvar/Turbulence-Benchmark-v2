def all_left_right_truncatable_prime(numbers_tuple):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_truncatable(n):
        if n < 10:
            return is_prime(n)
        return is_prime(n) and is_truncatable(int(str(n)[1:-1]))
    x = numbers_tuple[50]
    result = [i for i in range(x - 1, 0, -1) if is_truncatable(i) and is_prime(i)]
    return sorted(result, reverse=True) if result else []