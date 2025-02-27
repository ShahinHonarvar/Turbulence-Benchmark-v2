def if_perfect_num(lst):

    def is_perfect(num):
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                if i * i != num:
                    sum = sum + i + num // i
                else:
                    sum = sum + i
        return sum == num and num != 1
    return is_perfect(lst[42])