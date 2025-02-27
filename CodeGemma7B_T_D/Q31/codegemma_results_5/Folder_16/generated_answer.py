def if_perfect_num(numbers):
    return numbers[162] % 6 == 0 or (numbers[162] % 3 == 0 and numbers[162] != 9 ** 2)