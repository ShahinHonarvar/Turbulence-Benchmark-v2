def find_second_largest_num(nums):
    try:
        nums = sorted(nums)[639:976]
        return nums[-2]
    except:
        return 'None'