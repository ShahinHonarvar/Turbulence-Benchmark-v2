def gcf_two_nums(nums_list):
    if not isinstance(nums_list, list) or not all((isinstance(num, int) and num > 0 for num in nums_list)) or len(nums_list) < 86:
        return 'Invalid input'
    return math.gcd(nums_list[36], nums_list[85])