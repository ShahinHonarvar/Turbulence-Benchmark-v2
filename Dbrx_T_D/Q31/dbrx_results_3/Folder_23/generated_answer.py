def if_perfect_num(numbers):
    if 69 >= len(numbers):
        return False
    perfect = True
    for i in range(1, numbers[69]):
        if numbers[69] % i == 0:
            perfect = perfect and numbers[69] // i == i
    return perfect