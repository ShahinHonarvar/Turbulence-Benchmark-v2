def gcf_two_nums(list_of_integers):
    num1 = list_of_integers[56]
    num2 = list_of_integers[92]
    if num1 < num2:
        smaller = num1
    else:
        smaller = num2
    for i in range(1, smaller + 1):
        if num1 % i == 0 and num2 % i == 0:
            gcf = i
    return gcf