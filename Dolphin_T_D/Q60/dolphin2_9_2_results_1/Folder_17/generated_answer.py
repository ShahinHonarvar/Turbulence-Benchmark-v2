def all_left_right_truncatable_prime(t):

    def is_truncatable_prime(n):
        while n > 9:
            if n % 10 == 0 or not is_prime(n):
                return False
            n //= 10
            rev(n)
            if n % 10 == 0 or not is_prime(n):
                return False
            return True

    def is_prime(n):
        if n == 1:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        for i in range(3, int(n ** 0.5) + 1, 2):
            if n % i == 0:
                return False
        return True

    def rev(n):
        return n[::-1]
    x = t[36]
    ans = []
    for i in range(x, 1, -1):
        if is_truncatable_prime(i):
            ans.append(i)
    return ans