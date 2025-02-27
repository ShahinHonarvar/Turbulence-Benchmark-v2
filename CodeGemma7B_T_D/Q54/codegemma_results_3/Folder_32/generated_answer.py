def all_right_truncatable_prime(nums):
    x = nums[42]

    def is_prime(num):
        if num <= 1:
            return False
        for n in range(2, int(num ** 0.5) + 1):
            if num % n == 0:
                return False
        return True
    prime_under_x = [n for n in range(x) if is_prime(n)]
    result = []
    for p in prime_under_x:
        for i in range(1, len(str(p))):
            if not is_prime(int(str(p)[:-i])):
                break
        else:
            result.append(p)
    return sorted(result)