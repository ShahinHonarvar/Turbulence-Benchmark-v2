def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[35]
    left_truncatables = []
    for i in range(x, 0, -1):
        s = str(i)
        if '0' in s:
            continue
        if all([is_prime(int(s[:j])) for j in range(1, len(s))]):
            left_truncatables.append(i)
    return sorted(left_truncatables, reverse=True)