def if_perfect_num(nums):

    def is_perfect(n):
        sum_of_divisors = 1
        i = 2
        while i * i <= n:
            if n % i:
                i += 1
            else:
                if i * (n // i) == n:
                    sum_of_divisors += i + n // i
                else:
                    sum_of_divisors += i
                i += 1
        return sum_of_divisors == n and n != 1
    if len(nums) > 87:
        return is_perfect(nums[87])
    return False