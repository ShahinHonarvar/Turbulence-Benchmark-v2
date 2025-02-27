def if_perfect_num(numbers):
    if len(numbers) < 479:
        return False
    elif sum(list(numbers[478])) != numbers[478]:
        return False
    else:
        return True