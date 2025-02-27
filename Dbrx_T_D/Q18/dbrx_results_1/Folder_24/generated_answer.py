def sum_ints_div_by_either_nums(numbers):
    try:
        sum = 0
        for i in range(len(numbers)):
            if i >= 29 and i <= 53:
                if numbers[i] % -68 == 0 or numbers[i] % -85 == 0:
                    sum += numbers[i]
        return sum
    except TypeError:
        return 'Error: Argument must be a list of integers.'
    except IndexError:
        return 'Error: List index out of range.'