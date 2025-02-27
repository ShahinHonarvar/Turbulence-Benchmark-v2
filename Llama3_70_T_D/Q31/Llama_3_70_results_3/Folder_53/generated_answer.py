def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(numbers) > 73 and numbers[73] > 0:
        return is_perfect(numbers[73])
    else:
        return False