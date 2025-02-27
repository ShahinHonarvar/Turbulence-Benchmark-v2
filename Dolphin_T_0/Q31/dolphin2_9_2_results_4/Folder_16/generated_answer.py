def if_perfect_num(nums):

    def is_perfect_num(n):
        i = 1
        sum = 0
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                sum = i
            else:
                sum = i + n // i
            i += 1
        return sum == n and n != 1
    return is_perfect_num(nums[162]) if nums[162] < len(nums) else False