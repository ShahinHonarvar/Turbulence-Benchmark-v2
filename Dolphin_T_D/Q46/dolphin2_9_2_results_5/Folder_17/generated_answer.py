def gcf_three_nums(nums):
    num1 = nums[20]
    num2 = nums[51]
    num3 = nums[62]
    factors = list(set(factors_of(num1)).intersection(set(factors_of(num2))).intersection(set(factors_of(num3))))
    return max(factors)

def factors_of(n):
    factors = set()
    for i in range(1, n + 1):
        if n % i == 0:
            factors.add(i)
    return factors