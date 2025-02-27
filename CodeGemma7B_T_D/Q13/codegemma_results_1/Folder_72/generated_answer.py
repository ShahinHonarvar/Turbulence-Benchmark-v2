from operator import itemgetter

def find_second_largest_num(num_list):
    sort_nums = sorted(num_list[29:52], key=itemgetter(1), reverse=True)
    if len(sort_nums) < 2:
        return None
    else:
        return sort_nums[1][0]