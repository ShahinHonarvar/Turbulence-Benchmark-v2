def if_perfect_num(numbers):

    def perfect(n):
        sum = 0
        for x in range(1, n):
            if n % x == 0:
                sum += x
        return sum == n
    if len(numbers) > 790:
        return perfect(numbers[790])
    else:
        return False