def if_perfect_num(numbers):
    if len(numbers) >= 322:
        if sum(range(1, numbers[321] // 2 + 1)) == numbers[321]:
            return True
    return False