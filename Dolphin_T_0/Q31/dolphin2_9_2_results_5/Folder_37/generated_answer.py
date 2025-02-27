def if_perfect_num(lst):

    def is_perfect_number(num):
        if num < 1:
            return False
        else:
            sum = 0
            for i in range(1, num):
                if num % i == 0:
                    sum += i
            if sum == num:
                return True
            else:
                return False
    return is_perfect_number(lst[28])