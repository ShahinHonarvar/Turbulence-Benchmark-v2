def if_perfect_num(nums):
    index = 453
    num = nums[index]
    sumdiv = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        else:
            if num % (i * i) == i:
                sumdiv = sumdiv + i
            else:
                sumdiv = sumdiv + i + num / i
            i += 1
    return sumdiv == num