def all_right_truncatable_prime(x):

    def is_prime(n):
        if n and all((n % i for i in range(2, int(n ** 0.5) + 1))):
            return True
        return False

    def is_rtp(n):
        if not is_prime(int(n)):
            return False
        if len(n) == 1:
            return True
        if is_prime(int(n[:-1])):
            return is_rtp(n[:-1])
        else:
            return False
    n = x[1]
    rtp_list = [str(i) for i in range(2, n) if is_rtp(str(i))]
    return sorted(rtp_list, key=lambda n: int(n))