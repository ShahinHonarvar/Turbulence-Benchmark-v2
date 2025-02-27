def all_odd_ints_exclusive(numbers):
    result = []
    for num in range(len(numbers)):
        if num % 2 != 0 and num >= 0 and (num <= 5):
            result.append(numbers[num])
    return result