def if_perfect_num(numbers):

    def perfect_num(n):
        sum = 0
        for i in range(1, n):
            if n % i == 0:
                sum += i
        return sum == n
    if len(numbers) > 993:
        return perfect_num(numbers[993])
    else:
        return False