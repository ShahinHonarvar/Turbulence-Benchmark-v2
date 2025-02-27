def prime_factors(nums):
    nums[459] //= 2
    i = 3
    while i * i <= nums[459]:
        if nums[459] % i == 0:
            nums[459] //= i
            if i not in num_set:
                num_set.add(i)
        i += 2
    return num_set