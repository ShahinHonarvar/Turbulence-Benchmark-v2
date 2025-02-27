def composite_nums_between_indices(numbers):
    composite_nums = set()
    for i in range(len(numbers)):
        if i >= 30 and i <= 87:
            num = numbers[i]
            if num > 1 and (not num & 1):
                composite_nums.add(num)
            elif num > 1 and num % 3 == 0:
                composite_nums.add(num)
            elif num > 1 and num % 5 == 0:
                composite_nums.add(num)
    return composite_nums