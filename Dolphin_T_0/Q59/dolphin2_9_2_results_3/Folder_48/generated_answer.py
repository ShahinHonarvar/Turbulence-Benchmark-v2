def all_left_truncatable_prime(numbers):
    x = numbers[835]
    prime_numbers = []
    for number in range(2, x):
        if number > 1:
            for i in range(2, number):
                if number % i == 0:
                    break
            else:
                check = True
                temp = number
                while temp > 0:
                    if temp % 10 == 0:
                        check = False
                        break
                    temp = int(temp / 10)
                if check:
                    left_truncutable = True
                    for f in range(2, len(str(number)) + 1):
                        if not is_prime(int(str(number)[f - 1:])):
                            left_truncutable = False
                            break
                    if left_truncutable:
                        prime_numbers.append(number)
    prime_numbers.sort()
    return prime_numbers

def is_prime(n):
    if n > 1:
        for i in range(2, n):
            if n % i == 0:
                return False
        else:
            return True
    else:
        return False