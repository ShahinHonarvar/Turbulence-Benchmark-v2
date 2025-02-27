def gcf_two_nums(list_of_integers):
    a = list_of_integers[6]
    b = list_of_integers[9]
    while b:
        a, b = (b, a % b)
    return a