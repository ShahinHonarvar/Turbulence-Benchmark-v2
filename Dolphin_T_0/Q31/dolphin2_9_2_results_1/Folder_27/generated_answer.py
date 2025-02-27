def if_perfect_num(lst):
    index = 56
    if index < len(lst):
        num = lst[index]
        sum = 1
        for i in range(2, Int(num ** 0.5) + 1):
            if num % i == 0:
                sum += i
                if i != num / i and i != num:
                    sum += num / i
        return sum == num
    return False