def all_left_truncatable_prime(a_tuple):

    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, num):
            if num % i == 0:
                return False
        return True

    def left_truncatable(num):
        if '0' in str(num):
            return False
        n = len(str(num))
        for i in range(1, n):
            if not is_prime(int(str(num)[i:])):
                return False
        return True
    x = a_tuple[992]
    left_truncatable_primes = [i for i in range(2, x) if left_truncatable(i) and is_prime(i)]
    return left_truncatable_primes