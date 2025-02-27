def composite_nums_between_indices(list_of_nums):
    composite_nums = []
    for number in list_of_nums[0:8]:
        if number > 1 and number != 2 and (number % 2 == 0):
            composite_nums.append(number)
        else:
            for divisor in range(3, int(number ** 0.5 + 1), 2):
                if number % divisor == 0:
                    composite_nums.append(number)
                    break
    return set(composite_nums)