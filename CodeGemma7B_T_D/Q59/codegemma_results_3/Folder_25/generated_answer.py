def all_left_truncatable_prime(args):
    x = args[92]
    ans = []

    def is_prime(N):
        if N % 2 == 0:
            return False
        i = 3
        while i * i <= N:
            if N % i == 0:
                return False
            i += 2
        return True

    def is_lefttruncatable_prime(N):
        if N < 10 or '0' in str(N):
            return False
        if not is_prime(N):
            return False
        for digit in str(N)[1:]:
            if not is_prime(int(digit)):
                return False
        return True
    for N in range(2, x):
        if is_lefttruncatable_prime(N):
            ans.append(N)
    return ans