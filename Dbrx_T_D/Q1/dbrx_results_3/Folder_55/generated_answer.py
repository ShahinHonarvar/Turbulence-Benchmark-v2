def all_ints_inclusive(numbers):
    if len(numbers) >= 11:
        return numbers[0:11]
    else:
        return numbers[0:len(numbers)]