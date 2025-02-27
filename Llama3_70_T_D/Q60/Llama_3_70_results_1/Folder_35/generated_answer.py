def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncatable_prime(n, left, right):
        if n < 10:
            return is_prime(n)
        if '0' in str(n):
            return False
        return truncatable_prime(int(str(n)[left:right]), left + 1, right - 1) and is_prime(n)
    x = nums[177]
    return sorted([i for i in range(2, x + 1) if truncatable_prime(i, 0, len(str(i)))])