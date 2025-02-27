def all_left_right_truncatable_prime(numbers):
    x = numbers[175]
    primes = [2, 3, 5, 7]
    for number in range(10, x + 1):
        if all((number % digit != 0 for digit in range(2, number))):
            str_num = str(number)
            if not any(('0' in str_num[i:j] for i in range(len(str_num)) for j in range(i + 1, len(str_num) + 1))):
                while len(str_num) > 1:
                    str_num = str_num[1:-1]
                    if int(str_num) in primes:
                        primes.append(number)
                    elif int(str_num) not in primes:
                        break
    if primes:
        return sorted(list(set(primes)))
    else:
        return []