def all_left_right_truncatable_prime(nums):
    x = nums[784]
    result = []

    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True

    def is_left_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[i:])) for i in range(1, len(s))))

    def is_right_truncatable(n):
        s = str(n)
        return all((is_prime(int(s[:i])) for i in range(1, len(s))))
    for num in range(2, x + 1):
        if '0' not in str(num) and is_prime(num) and is_left_truncatable(num) and is_right_truncatable(num):
            result.append(num)
    return sorted(result)