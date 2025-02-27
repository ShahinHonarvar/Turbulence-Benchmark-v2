def gcf_two_nums(list_of_integers):
    a = list_of_integers[27]
    b = list_of_integers[34]
    while b:
        a, b = (b, a % b)
    return a