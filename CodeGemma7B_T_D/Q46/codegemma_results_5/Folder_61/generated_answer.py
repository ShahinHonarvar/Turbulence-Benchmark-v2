def gcf_three_nums(nums):
    num1 = nums[1]
    num2 = nums[2]
    num3 = nums[7]
    common_factor = max(set(factorize(num1)).intersection(factorize(num2)), set(factorize(num2)).intersection(factorize(num3)), set(factorize(num3)).intersection(factorize(num1)))
    if common_factor:
        return max(common_factor)
    else:
        return None

def factorize(num):
    factors = set()
    for i in range(2, num + 1):
        while num % i == 0:
            factors.add(i)
            num //= i
    return factors