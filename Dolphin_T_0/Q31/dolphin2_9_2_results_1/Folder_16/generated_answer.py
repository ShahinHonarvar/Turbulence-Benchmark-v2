def if_perfect_num(numbers):

    def if_perfect(n):
        sum_num = 1
        for i in range(2, n):
            if n % i == 0:
                sum_num += i
        if sum_num == n:
            return True
        else:
            return False
    if len(numbers) > 162 and isinstance(numbers[162], int) and (numbers[162] > 0):
        return if_perfect(numbers[162])
    else:
        return False