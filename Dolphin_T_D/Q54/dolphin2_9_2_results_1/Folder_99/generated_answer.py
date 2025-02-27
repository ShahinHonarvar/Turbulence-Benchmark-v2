def all_right_truncatable_prime(num):

    def check_prime(n):
        if n == 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def check_right_truncatable(n):
        while n > 0:
            if not check_prime(n):
                return False
            n //= 10
        return True
    x = num[758]
    ans = [i for i in range(2, x) if check_prime(i) and i % 10 != 0 and check_right_truncatable(i)]
    return sorted(ans)