def if_perfect_num(list_of_integers):
    num = list_of_integers[702]
    sum = 1
    i = 2
    while i * i <= num:
        if num % i:
            i += 1
        elif i * (num // i) == num:
            sum = sum + i + num // i
            i += 1
        else:
            sum += i
            i += 1
    return sum == num and num != 1