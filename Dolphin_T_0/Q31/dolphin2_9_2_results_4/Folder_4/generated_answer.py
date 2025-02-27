def if_perfect_num(lst):

    def is_perfect(num):
        if num < 1:
            return False
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        if sum == num:
            return True
        return False
    if is_perfect(lst[15]):
        return True
    return False