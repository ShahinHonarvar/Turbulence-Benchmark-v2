def if_perfect_num(nums):

    def is_perfect(n):
        sum = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                if i * i != n:
                    sum = sum + i + n / i
                else:
                    sum = sum + i
        return sum == n and n != 1
    return is_perfect(nums[23]) if len(nums) > 23 else False