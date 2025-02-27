def if_perfect_num(nums):

    def is_perfect(num):
        if num < 6:
            return False
        sum_div = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum_div = sum_div + i + num // i
                else:
                    sum_div = sum_div + i
                i += 1
        return sum_div == num and num != 1
    return is_perfect(nums[993])