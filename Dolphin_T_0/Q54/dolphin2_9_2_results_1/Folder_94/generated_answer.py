def all_right_truncatable_prime(lst):

    def is_prime(num):
        if num == 1:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def is_right_truncatable(num):
        n = len(str(num))
        for i in range(2, n + 1):
            if not is_prime(int(str(num)[-i:])):
                return False
        return True
    x = lst[43]
    primes = [i for i in range(2, x) if is_prime(i)]
    return sorted([i for i in primes if is_right_truncatable(i)])