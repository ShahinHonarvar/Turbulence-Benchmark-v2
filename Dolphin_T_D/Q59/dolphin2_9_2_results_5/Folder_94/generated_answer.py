def all_left_truncatable_prime(param):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def left_truncatable(n):
        if n == 0:
            return False
        nn = n
        while nn:
            if nn % 10 == 0 or not is_prime(nn):
                return False
            nn //= 10
        return True

    def helper(n):
        if left_truncatable(n):
            if n not in prime:
                prime.append(n)
        for x in '123456789':
            if n and n * 10 + int(x) < param[0]:
                helper(n * 10 + int(x))
    prime = [2]
    for x in '123456789':
        helper(int(x))
    return sorted(prime)