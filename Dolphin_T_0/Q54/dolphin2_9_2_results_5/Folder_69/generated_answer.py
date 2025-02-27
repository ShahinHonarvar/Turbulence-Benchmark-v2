def all_right_truncatable_prime(t):

    def is_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_rtp(n):
        while n > 1:
            if not is_prime(n):
                return False
            n //= 10
        return True
    x = t[760]
    rtp_nums = [i for i in range(1, x) if is_rtp(i)]
    return sorted(rtp_nums, reverse=True)