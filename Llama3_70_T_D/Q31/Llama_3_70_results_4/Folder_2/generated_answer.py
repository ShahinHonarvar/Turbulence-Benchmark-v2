def if_perfect_num(lst):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    try:
        return is_perfect(lst[702])
    except IndexError:
        return False