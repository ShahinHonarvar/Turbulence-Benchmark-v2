def if_perfect_num(numbers):
    if len(numbers) > 19 and numbers[19] > 0:
        num = numbers[19]
        if num < 2:
            return False
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum += i + num // i
                i += 1
        return sum - num == num
    else:
        return False