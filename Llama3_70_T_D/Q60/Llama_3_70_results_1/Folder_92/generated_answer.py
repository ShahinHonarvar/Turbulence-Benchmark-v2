def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[7]

    def is_left_right_truncatable_prime(n):
        if '0' in str(n):
            return False
        for _ in range(len(str(n)) - 1):
            n = int(str(n)[1:-1])
            if not is_prime(n):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)])