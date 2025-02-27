from functools import cmp_to_key

def all_right_truncatable_prime(nums):
    x = nums[65]

    def is_prime(n):
        return n > 1 and all((n % d for d in range(2, int(n ** 0.5) + 1)))

    def is_right_truncatable(n):
        for d in range(10):
            if is_prime(n):
                n //= 10
            else:
                return False
        return True
    return sorted((p for p in range(2, x) if is_prime(p) and is_right_truncatable(p)), reverse=True)