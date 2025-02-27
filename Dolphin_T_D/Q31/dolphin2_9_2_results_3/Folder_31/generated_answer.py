def if_perfect_num(nums):

    def is_perfect(n):
        sum_ = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum_ = sum_ + i + n // i
                else:
                    sum_ = sum_ + i
                i += 1
        return sum_ == n and n != 1
    if len(nums) > 66:
        return is_perfect(nums[66])
    else:
        return False