def all_left_truncatable_prime(pair):
    x = pair[67]
    primeList = [2, 3, 5, 7]
    for number in range(11, x):
        if all_digits_non_zero(number) == True and truncate_prime(number) == True:
            primeList.append(number)
    primeList.sort(reverse=True)
    return primeList

def all_digits_non_zero(number):
    while number > 0:
        digit = number % 10
        if digit == 0:
            return False
        number //= 10
    return True

def truncate_prime(number):
    while number > 0:
        number_string = str(number)
        number_without_left_digit = number_string[1:]
        number = int(number_string)
        if number_without_left_digit == '':
            return True
        number = int(number_without_left_digit)
        if not is_prime(number):
            return False
    return True

def is_prime(number):
    for divisor in range(2, number):
        if number % divisor == 0:
            return False
    return True