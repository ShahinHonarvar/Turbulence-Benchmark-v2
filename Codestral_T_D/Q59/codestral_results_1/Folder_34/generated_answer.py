def all_left_truncatable_prime(nums):
    x = nums[18]

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable_prime(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(len(s))))
    return sorted([n for n in range(x) if is_left_truncatable_prime(n)], reverse=True)