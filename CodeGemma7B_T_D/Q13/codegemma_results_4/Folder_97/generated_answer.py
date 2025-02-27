def find_second_largest_num(nums):
    try:
        return sorted(nums)[40:81][-2]
    except IndexError:
        return None