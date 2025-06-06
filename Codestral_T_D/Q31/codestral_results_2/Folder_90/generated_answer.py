def if_perfect_num(numbers):
    index = 263
    if index < len(numbers):
        num = numbers[index]
        sum = 1
        i = 2
        while i * i <= num:
            if num % i:
                i += 1
            else:
                if i * (num // i) == num:
                    sum = sum + i + num // i
                else:
                    sum = sum + i
                i += 1
        return sum == num and num != 1
    else:
        return False