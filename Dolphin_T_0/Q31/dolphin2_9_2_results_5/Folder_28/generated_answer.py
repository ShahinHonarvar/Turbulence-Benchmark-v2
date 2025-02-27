def if_perfect_num(nums):

    def is_perfect(n):
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if n % (i * i) != i:
                    sum = sum + i
                i += 1
        return sum == n and n != 1
    return is_perfect(nums[37])