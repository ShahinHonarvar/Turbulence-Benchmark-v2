def all_left_right_truncatable_prime(nums):

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
    x = nums[85]
    res = []
    for i in range(x, 1, -1):
        if is_prime(i):
            left = i
            while left > 9:
                left //= 10
                if not is_prime(left):
                    break
            if left > 9:
                left = 0
                while i % 10 == 0:
                    i //= 10
                    left += 1
                right = i % 10
                i = i // 10
                while i > 0 and is_prime(i):
                    if i < right:
                        res.append(i)
                    i = i // 10
                    left -= 1
    return res