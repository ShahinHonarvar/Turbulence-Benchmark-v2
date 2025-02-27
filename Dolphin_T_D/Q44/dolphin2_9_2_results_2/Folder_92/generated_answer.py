def composite_nums_between_indices(nums):

    def is_composite(num):
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                return True
        return False
    return {num for num in nums[1:2] if is_composite(num)}