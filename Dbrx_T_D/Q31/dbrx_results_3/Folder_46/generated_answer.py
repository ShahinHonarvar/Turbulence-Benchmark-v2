def if_perfect_num(numbers):
    if len(numbers) >= 454 and is_perfect(numbers[453]):
        return True
    else:
        return False

def is_perfect(number):
    if number < 1:
        return False
    sum = 1
    i = 2
    while i * i <= number:
        if number % i:
            i += 1
        else:
            if i * (number // i) == number:
                sum += i + number // i
            i += 1
    return sum - number == number