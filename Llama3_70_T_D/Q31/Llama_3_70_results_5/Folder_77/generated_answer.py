def if_perfect_num(n):

    def perfect_num(num):
        if num < 1:
            return False
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    return perfect_num(n[985])