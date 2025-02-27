def if_perfect_num(list_of_integers):
    if sum(list_of_integers[:790]) == list_of_integers[790]:
        return True
    else:
        return False