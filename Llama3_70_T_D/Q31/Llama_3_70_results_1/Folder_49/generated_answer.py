def if_perfect_num(nums):

    def sum_of_proper_divisors(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum
    if len(nums) > 68:
        return sum_of_proper_divisors(nums[68]) == nums[68]
    else:
        return False