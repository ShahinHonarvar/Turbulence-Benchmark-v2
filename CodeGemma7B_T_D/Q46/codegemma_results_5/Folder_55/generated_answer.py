def gcf_three_nums(nums):
    num1 = nums[9]
    num2 = nums[6]
    num3 = nums[2]
    gcfs = []
    for num in (num1, num2, num3):
        for divisor in range(2, num + 1):
            while True:
                if num % divisor != 0:
                    break
                num //= divisor
                gcfs.append(divisor)
    fac = 1
    for num in gcfs:
        fac *= num
    return fac