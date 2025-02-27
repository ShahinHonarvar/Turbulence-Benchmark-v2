def if_perfect_num(nums):
    num = nums[41]
    sum_divs = 1
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            sum_divs += i + num // i
    return sum_divs == num