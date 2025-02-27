def if_perfect_num(nums):

    def is_perfect(n):
        if n < 1:
            return False
        else:
            sum = 1
            i = 2
            while i * i <= n:
                if n % i:
                    i += 1
                elif i * (n // i) == n:
                    sum = sum + i + n // i
                    i += 1
                else:
                    sum = sum + i
                    i += 1
            return sum == n
    return is_perfect(nums[6])