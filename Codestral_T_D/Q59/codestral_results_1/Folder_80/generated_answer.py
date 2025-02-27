def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n <= 1 or '0' in str(n):
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[14]
    result = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            truncated = str(num)
            while len(truncated) > 0:
                if not is_prime(int(truncated)):
                    break
                truncated = truncated[1:]
            else:
                result.append(num)
    return sorted(result, reverse=True)