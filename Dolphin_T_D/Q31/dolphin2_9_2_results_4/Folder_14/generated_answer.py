def if_perfect_num(numbers):

    def is_perfect(num):
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            elif i * (num // i) == num:
                sum = sum + i + num // i
                i += 1
            else:
                sum = sum + i
                i += 1
        return sum == num and num != 1
    return is_perfect(numbers[17])