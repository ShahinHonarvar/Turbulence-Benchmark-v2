def if_perfect_num(lst):

    def is_perfect(num):
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return sum == num
    if len(lst) > 828 and is_perfect(lst[828]):
        return True
    else:
        return False