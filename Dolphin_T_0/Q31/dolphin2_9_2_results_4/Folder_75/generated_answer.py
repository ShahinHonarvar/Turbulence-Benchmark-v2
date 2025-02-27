def if_perfect_num(list_of_ints):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    return is_perfect(list_of_ints[80])