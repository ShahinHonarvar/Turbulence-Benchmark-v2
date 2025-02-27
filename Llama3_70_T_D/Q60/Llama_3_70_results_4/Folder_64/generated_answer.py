def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for length in range(2, len(n_str) + 1):
            for i in range(len(n_str) - length + 1):
                trunc = n_str[i:i + length]
                if not is_prime(int(trunc)):
                    return False
        return True
    x = nums[4]
    return sorted([i for i in range(2, x + 1) if is_left_right_truncatable_prime(i)])