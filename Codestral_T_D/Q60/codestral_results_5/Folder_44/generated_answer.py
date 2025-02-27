def all_left_right_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def truncate_left(n):
        return int(str(n)[1:])

    def truncate_right(n):
        return int(str(n)[:-1])
    x = nums[39]
    result = []
    for n in range(2, x + 1):
        if not is_prime(n):
            continue
        if '0' in str(n):
            continue
        truncated = truncate_left(n)
        while truncated > 0:
            if not is_prime(truncated):
                break
            truncated = truncate_left(truncated)
        else:
            truncated = truncate_right(n)
            while truncated > 0:
                if not is_prime(truncated):
                    break
                truncated = truncate_right(truncated)
            else:
                result.append(n)
    result.sort()
    return result