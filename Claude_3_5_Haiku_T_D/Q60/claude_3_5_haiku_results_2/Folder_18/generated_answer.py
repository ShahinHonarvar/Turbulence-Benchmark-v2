def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(nums):
    x = nums[429]
    result = []

    def is_left_right_truncatable(n):
        if '0' in str(n):
            return False
        while n > 9:
            n_str = str(n)
            n = int(n_str[1:])
            if not is_prime(n):
                return False
        n_str = str(n)
        for d in n_str:
            curr = int(d)
            if not is_prime(curr):
                return False
        return True
    for num in range(x, 11, -1):
        if is_prime(num) and is_left_right_truncatable(num):
            result.append(num)
    return result