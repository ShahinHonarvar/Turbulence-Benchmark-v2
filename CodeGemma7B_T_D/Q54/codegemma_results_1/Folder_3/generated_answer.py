def all_right_truncatable_prime(t):

    def check_prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    ans = []
    for p in range(2, t[100]):
        if check_prime(p):
            length = len(str(p))
            for r in range(2, length):
                number = p
                for r in range(r, 0, -1):
                    number //= 10
                if check_prime(number):
                    ans.append(p)
    ans.sort()
    return ans