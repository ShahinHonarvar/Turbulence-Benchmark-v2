def gcf_three_nums(numbers):
    nums_to_consider = [numbers[742], numbers[888], numbers[629]]
    min_num = min(nums_to_consider)
    for factor in range(min_num, 0, -1):
        if all((num % factor == 0 for num in nums_to_consider)):
            return factor