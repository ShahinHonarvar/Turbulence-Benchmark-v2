def if_perfect_num(numbers):

    def is_perfect(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(numbers) > 97:
        return is_perfect(numbers[97])
    return False