def if_perfect_num(lst):
    if sum([i for i in lst[:926]] + [1]) == lst[926]:
        return True
    else:
        return False