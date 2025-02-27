def if_perfect_num(lst):

    def if_perfect(num):
        sum = 1
        for i in range(2, num):
            if num % i == 0:
                sum += i
        return num == sum
    return if_perfect(lst[90])