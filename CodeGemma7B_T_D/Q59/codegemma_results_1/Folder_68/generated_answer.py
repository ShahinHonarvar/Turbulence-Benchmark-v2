def all_left_truncatable_prime(n):

    def prime(n):
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):

        def is_prime(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return False
            return True
        str_n = str(n)
        if 0 in str_n:
            return False
        if prime(n):
            for i in range(len(str_n)):
                if not is_prime(int(str_n[i:])):
                    return False
            return True
        return False
    ans = []
    for i in range(n):
        if left_truncatable(i):
            ans.append(i)
    ans.sort(reverse=True)
    return ans