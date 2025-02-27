def all_left_truncatable_prime(nums):

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    x = nums[0]
    result = []
    for num in range(x, 1, -1):
        num_str = str(num)
        is_truncatable = True
        for i in range(len(num_str)):
            if not is_prime(int(num_str[i:])):
                is_truncatable = False
                break
        if is_truncatable and '0' not in num_str:
            result.append(num)
    return sorted(result, reverse=True)