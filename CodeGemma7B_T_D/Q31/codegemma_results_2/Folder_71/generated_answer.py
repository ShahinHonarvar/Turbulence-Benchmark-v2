def if_perfect_num(nums):

    def is_perfect(n):
        sum_of_div = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_of_div += i + n // i
        return sum_of_div == n
    if is_perfect(nums[78]):
        return True
    else:
        return False