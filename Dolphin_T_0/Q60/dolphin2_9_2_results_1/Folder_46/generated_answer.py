def all_left_right_truncatable_prime(inp):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_and_right_truncatable(n):
        while len(str(n)) > 2:
            if not is_prime(n):
                return False
            n = int(str(n)[1:-1])
        return is_prime(n)
    x = inp[33]
    result = [i for i in range(2, x + 1) if left_and_right_truncatable(i)]
    return result