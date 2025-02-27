def gcf_three_nums(numbers):
    nums_to_consider = [numbers[20], numbers[35], numbers[74]]
    divisor = min(nums_to_consider)
    while divisor > 0:
        if all((num % divisor == 0 for num in nums_to_consider)):
            return divisor
        divisor -= 1