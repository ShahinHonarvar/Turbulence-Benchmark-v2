def if_perfect_num(numbers):
    num = numbers[21]
    if num > 0:
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            elif i * (num / i) == num:
                sum = sum + i + num / i
                i += 1
            else:
                sum = sum + i
                i += 1
        return sum == num
    else:
        return False