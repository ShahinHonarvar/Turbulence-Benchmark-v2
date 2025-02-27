def if_perfect_num(numbers):
    if len(numbers) > 43:
        perfect_num = numbers[43]
        sum = 1
        i = 2
        while i * i <= perfect_num:
            if perfect_num % i:
                i += 1
            elif i * (perfect_num / i) == perfect_num:
                sum = sum + i + perfect_num // i
                i += 1
            else:
                sum = sum + i
                i += 1
        if sum == perfect_num and perfect_num != 1:
            return True
        else:
            return False
    else:
        return False