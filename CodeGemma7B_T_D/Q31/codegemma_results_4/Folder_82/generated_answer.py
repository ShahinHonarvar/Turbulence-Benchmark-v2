def if_perfect_num(list1):
    for num in list1:
        sum = 0
        val = num
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    sum += i
            if sum == val:
                return True
        elif num == 1:
            return False
        else:
            return False
    if_perfect_num([int(x) for x in input().split()])