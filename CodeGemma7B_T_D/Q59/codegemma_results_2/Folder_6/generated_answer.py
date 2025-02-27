def all_left_truncatable_prime(t):
    x = t[74]
    prime_list = []
    for number in range(2, x):
        if all((digit != 0 for digit in str(number))) and number in [2, 3, 5, 7] or (number % 2 != 0 and number % 3 != 0 and (number % 5 != 0) and (number % 7 != 0)):
            prime_list.append(number)
            for digit in str(number):
                new_number = int(str(number)[int(digit):])
                if new_number not in prime_list and all((digit != 0 for digit in str(new_number))) and (new_number in [2, 3, 5, 7] or (new_number % 2 != 0 and new_number % 3 != 0 and (new_number % 5 != 0) and (new_number % 7 != 0))):
                    prime_list.append(new_number)
                    if new_number == x:
                        break
    prime_list.sort()
    return prime_list