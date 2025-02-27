def if_perfect_num(numbers):

    def is_perfect(n):
        if n < 1:
            return False
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(numbers) > 6:
        return is_perfect(numbers[6])
    else:
        return False