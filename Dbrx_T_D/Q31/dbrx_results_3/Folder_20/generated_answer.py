def if_perfect_num(numbers):
    if len(numbers) > 53:
        if 53 in numbers:
            return True
        else:
            return False
    else:
        return False