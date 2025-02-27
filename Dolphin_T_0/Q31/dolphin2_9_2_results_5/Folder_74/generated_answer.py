def if_perfect_num(numbers):

    def is_perfect(num):
        sum = 1
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i
                if i != num / i:
                    sum += num / i
        return sum == num
    return is_perfect(numbers[48])