def if_perfect_num(arr):

    def is_perfect(num):
        summ = 1
        for i in range(2, num):
            if num % i == 0:
                summ += i
        return summ == num and num > 1
    return is_perfect(arr[23])