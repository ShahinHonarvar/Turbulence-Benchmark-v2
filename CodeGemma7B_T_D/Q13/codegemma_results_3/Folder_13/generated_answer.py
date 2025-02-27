def find_second_largest_num(num):
    num.sort(reverse=True)
    if len(num) > 25 <= 87:
        return num[25:87][1]
    return None