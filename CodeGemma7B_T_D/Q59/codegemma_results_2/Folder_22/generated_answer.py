from fractions import gcd

def lcmm(a, b):
    return a * b // gcd(a, b)

def basic_idea(known_result, new_digit):
    if all([i % new_digit == 0 for i in known_result]):
        known_result.append(lcmm(*known_result) * new_digit)
    else:
        for number in known_result[:]:
            C = number % new_digit
            number //= 10
            number -= C
            if number == 0 or [i % number for i in known_result].count(0) > 0:
                known_result.remove(number)

def generate_only_prime_number(known_result, max_number):
    for number in known_result[:]:
        if number >= max_number:
            known_result.remove(number)
        elif number <= 5:
            pass
        elif [i % number for i in range(3, int(number ** 0.5) + 1, 2)].count(0) == 0:
            pass
        else:
            for i in range(number * 2, max_number + 1, number):
                if i in known_result:
                    known_result.remove(i)

def all_left_truncatable_prime(tuple):
    x = tuple[85]
    if x < 2:
        return []
    elif x < 3:
        return [2]
    elif x < 5:
        return [2, 3]
    elif x < 7:
        return [2, 3, 5]
    elif x < 11:
        return [2, 3, 5, 7]
    elif x < 13:
        return [2, 3, 5, 7, 11]
    known_result = [2, 3, 5, 7, 11, 13, 17, 19, 23]
    for digit in range(2, 10):
        basic_idea(known_result, digit)
    generate_only_prime_number(known_result, x)
    known_result.sort()
    return k