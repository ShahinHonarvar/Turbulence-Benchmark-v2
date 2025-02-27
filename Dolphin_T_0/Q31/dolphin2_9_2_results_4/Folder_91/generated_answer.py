def if_perfect_num(lst):
    try:
        num = lst[6]
        sum = 1
        for i in range(2, round(num ** 0.5) + 1):
            if num % i == 0:
                if i == num / i:
                    sum = sum + i
                else:
                    sum = sum + i + num / i
        if sum == num:
            return True
        else:
            return False
    except:
        return False