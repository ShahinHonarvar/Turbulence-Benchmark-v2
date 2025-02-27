def if_perfect_num(nums):

    def is_perfect(n):
        if n < 6:
            return False
        sum = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            elif i * (n // i) == n:
                sum = sum + i + n // i - 1
                i += 1
            else:
                sum += i
                i += 1
        return sum == n and n != 1
    return is_perfect(nums[926]) if 926 < len(nums) else False