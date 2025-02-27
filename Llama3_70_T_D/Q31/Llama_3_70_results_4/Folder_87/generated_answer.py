def if_perfect_num(n):

    def perfect_num(num):
        sum = 0
        for i in range(1, num):
            if num % i == 0:
                sum += i
        return sum == num
    if len(n) > 96 and n[96] > 0:
        return perfect_num(n[96])
    else:
        return False