def if_perfect_num(lst):

    def is_perfect_number(num):
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num
    if len(lst) > 13:
        return is_perfect_number(lst[13])
    else:
        return False