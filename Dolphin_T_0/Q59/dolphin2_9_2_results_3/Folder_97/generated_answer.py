def all_left_truncable_prime(nums):

    def is_prime(n):
        if n <= 1:
            return False
        elif n <= 3:
            return True
        elif n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncable(n):
        num_str = str(n)
        for i in range(len(num_str) - 1, 0, -1):
            if num_str[i] == '0':
                return False
            if not is_prime(int(num_str[i:])):
                return False
        return True
    x = nums[645]
    primes = [i for i in range(2, x) if is_prime(i)]
    return [i for i in primes if is_truncable(i)]