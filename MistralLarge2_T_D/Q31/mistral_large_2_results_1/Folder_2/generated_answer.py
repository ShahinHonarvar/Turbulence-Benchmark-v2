def if_perfect_num(nums):

    def is_perfect(n):
        if n < 2:
            return False
        sum_of_divisors = 1
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                sum_of_divisors += i
                if i != n // i:
                    sum_of_divisors += n // i
        return sum_of_divisors == n
    if len(nums) > 702:
        return is_perfect(nums[702])
    return False