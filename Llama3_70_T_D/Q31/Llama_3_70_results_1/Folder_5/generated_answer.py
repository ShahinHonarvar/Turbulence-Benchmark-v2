def if_perfect_num(num_list):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    try:
        return is_perfect(num_list[67])
    except IndexError:
        return False