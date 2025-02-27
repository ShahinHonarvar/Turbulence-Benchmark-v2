def all_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def right_truncatable_prime(n):
        return all((is_prime(int(str(n)[::-1][i:][::-1])) for i in range(len(str(n)))))
    x = nums[33]
    return sorted(filter(right_truncatable_prime, range(2, x)))