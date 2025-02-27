def if_perfect_num(list_of_nums):
    if list_of_nums[68] == perfect_num(list_of_nums[68]):
        return True
    else:
        return False

def perfect_num(num):
    sum = 0
    for i in range(num):
        if num % (i + 1) == 0:
            sum += i + 1
    if num == sum:
        return True
    else:
        return False