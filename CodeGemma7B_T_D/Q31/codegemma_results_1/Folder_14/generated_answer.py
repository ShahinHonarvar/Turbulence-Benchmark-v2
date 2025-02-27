def if_perfect_num(list):
    if len(list) != 18:
        return False
    else:
        result = 1
        for i in range(list[17]):
            if list[17] % i == 0:
                if i != list[17]:
                    result += i
        if result == list[17]:
            return True
        else:
            return False