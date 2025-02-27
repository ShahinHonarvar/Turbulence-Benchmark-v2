def is_prime(n):
    if n < 2:
        return False
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[39]

    def is_left_right_truncatable_prime(n):
        n_str = str(n)
        if '0' in n_str:
            return False
        for i in range(1, len(n_str)):
            if not is_prime(int(n_str[i:])) or not is_prime(int(n_str[:-i])):
                return False
        return True
    return sorted([i for i in range(2, x + 1) if is_prime(i) and is_left_right_truncatable_prime(i)])