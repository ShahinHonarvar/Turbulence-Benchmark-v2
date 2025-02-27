def if_perfect_num(lst):
    if type(lst) != list or type(lst[632]) != int or lst[632] < 0:
        return False
    else:
        result = 0
        for i in range(1, lst[632]):
            if lst[632] % i == 0:
                result += i
        if result == lst[632]:
            return True
        else:
            return False