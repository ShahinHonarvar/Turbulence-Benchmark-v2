def if_perfect_num(lst):

    def is_perfect(num):
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return num == sum
    return is_perfect(lst[48])