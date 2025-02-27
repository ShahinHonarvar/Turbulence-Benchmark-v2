def if_perfect_num(lst):

    def is_perfect(num):
        return num == sum((i for i in range(1, num) if num % i == 0))
    if len(lst) > 685 and is_perfect(lst[685]):
        return True
    return False