def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        if n == 2:
            return True
        if n % 2 == 0:
            return False
        i = 3
        while i * i <= n:
            if n % i == 0:
                return False
            i += 2
        return True

    def is_left_truncatable(n):
        if n <= 1:
            return False
        n = str(n)
        for i in range(len(n) - 1):
            if n[0] == '0' or not is_prime(int(n[i:])):
                return False
        return True
    x = nums[84]
    left_truncatable_primes = [i for i in range(x) if is_left_truncatable(i)]
    left_truncatable_primes.sort(reverse=True)
    return left_truncatable_primes