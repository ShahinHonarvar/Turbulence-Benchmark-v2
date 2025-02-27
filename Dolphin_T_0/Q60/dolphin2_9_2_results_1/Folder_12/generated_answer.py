def all_left_right_truncatable_prime(tup):

    def is_prime(n):
        for i in range(2, n):
            if n % i == 0:
                return False
        return True

    def left_right_truncatable(n):
        while len(str(n)) > 2:
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    x = tup[70]
    result = [i for i in range(2, x + 1) if left_right_truncatable(i) and is_prime(i)]
    return result[::-1] if result else []