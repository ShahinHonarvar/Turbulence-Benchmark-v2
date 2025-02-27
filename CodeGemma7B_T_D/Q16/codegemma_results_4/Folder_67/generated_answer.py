def sum_even_ints_inclusive(nums):
    """Sums the even integers from index 22 to index 50, inclusive."""
    two_two = nums[22]
    is_two_two_even = two_two % 2 == 0
    two_five = nums[50]
    is_two_five_even = two_five % 2 == 0
    sum_even = 0
    if is_two_two_even:
        if is_two_five_even:
            sum_even = (two_five + two_two) // 2 + 1
            for i in range(24, 51):
                odd_even = nums[i] % 2
                if not odd_even:
                    sum_even += nums[i]
        else:
            for i in range(24, 51):
                odd_even = nums[i] % 2
                if not odd_even:
                    if nums[i] < two_two:
                        continue
                    sum_even += nums[i]
    elif is_two_five_even:
        for i in range(24, 51):
            odd_even = nums[i] % 2
            if not odd_even:
                if nums[i] > two_five:
                    continue
                sum_even += nums[i]
    else:
        for i in range(24, 51):
            odd_even = nums[i] % 2
            if not odd_even:
                sum_even += nums[i]
    return sum_even