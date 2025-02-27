def all_left_right_truncatable_prime(nums):
    x = nums[3]

    def is_prime(n):
        if n <= 1:
            return False
        if n <= 3:
            return True
        if n % 2 == 0 or n % 3 == 0:
            return False
        i = 5
        while i * i <= n:
            if n % i == 0 or n % (i + 2) == 0:
                return False
            i += 6
        return True

    def is_truncatable_prime(n):
        if '0' in str(n):
            return False
        temp_left = temp_right = n
        digits = len(str(n))
        while temp_left and temp_right:
            if not is_prime(temp_left) or not is_prime(temp_right):
                return False
            temp_left //= 10
            div = 10 ** (digits - 1)
            temp_right %= div
            digits -= 1
        return True
    result = []
    for i in range(10, x + 1):
        if is_truncatable_prime(i):
            result.append(i)
    return sorted(result, reverse=True)