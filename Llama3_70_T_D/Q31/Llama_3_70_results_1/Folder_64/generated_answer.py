def if_perfect_num(n):

    def perfect_num(num):
        sum = 0
        for x in range(1, num):
            if num % x == 0:
                sum += x
        return sum == num
    return perfect_num(n[1])