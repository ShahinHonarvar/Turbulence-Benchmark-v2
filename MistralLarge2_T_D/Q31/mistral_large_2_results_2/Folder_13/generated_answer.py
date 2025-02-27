def if_perfect_num(nums):

    def is_perfect_number(n):
        if n < 2:
            return False
        divisors = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                divisors.append(i)
                if i != n // i:
                    divisors.append(n // i)
        return sum(divisors) == n
    if len(nums) > 126:
        return is_perfect_number(nums[126])
    return False