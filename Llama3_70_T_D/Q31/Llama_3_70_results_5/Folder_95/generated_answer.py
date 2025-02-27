def if_perfect_num(n):

    def is_perfect(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    if len(n) > 87 and n[87] > 0:
        return is_perfect(n[87])
    else:
        return False