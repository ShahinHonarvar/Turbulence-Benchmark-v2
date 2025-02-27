def all_left_right_truncatable_prime(t):
    x = t[429]
    primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]

    def is_prime(k):
        if k <= 1:
            return False
        for i in range(2, int(k ** 0.5)):
            if k % i == 0:
                return False
        return True

    def is_truncatable_prime(k):
        if k % 10 == 0 or k % 10 == 5 or is_prime(k) == False:
            return False
        for i in range(len(str(k)) - 1):
            k //= 10
            if is_prime(k) == False:
                return False
        return True
    ans = [i for i in primes if is_truncatable_prime(i) and i <= x]
    ans.sort(reverse=True)
    return ans or []