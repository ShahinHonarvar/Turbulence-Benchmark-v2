def if_perfect_num(numbers):
    if len(numbers) > 40:
        num = numbers[40]
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            elif i * (num // i) == num:
                sum = sum + i + num // i
            else:
                sum = sum + i
                i += 1
        return sum == num and num != 1
    else:
        return False