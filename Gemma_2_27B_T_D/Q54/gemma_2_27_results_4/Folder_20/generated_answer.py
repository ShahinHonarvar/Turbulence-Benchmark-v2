def all_right_truncatable_prime(nums):
    x = nums[100]

    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    res = []
    for i in range(x, 0, -1):
        if is_prime(i):
            temp = i
            while temp > 0:
                if not is_prime(temp):
                    break
                temp //= 10
            else:
                res.append(i)
    return sorted(res, reverse=True)