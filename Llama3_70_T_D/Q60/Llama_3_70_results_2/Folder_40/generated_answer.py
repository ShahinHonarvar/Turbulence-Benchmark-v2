def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):

    def truncatable_prime(n):
        str_n = str(n)
        for i in range(1, len(str_n)):
            if not is_prime(int(str_n[i:])) or not is_prime(int(str_n[:-i])):
                return False
        return True
    x = nums[10]
    return sorted([i for i in range(10, x + 1) if is_prime(i) and truncatable_prime(i) and ('0' not in str(i))], reverse=True)