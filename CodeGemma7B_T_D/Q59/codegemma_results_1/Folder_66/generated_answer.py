def all_left_truncatable_prime(args):
    result = []
    for i in range(args[25]):
        number = str(i)
        if number.count('0') == 0 and is_prime(number):
            is_truncatable = True
            for j in range(1, len(number)):
                if not is_prime(number[j:]):
                    is_truncatable = False
                    break
            if is_truncatable:
                result.append(number)
    result.sort(reverse=True)
    return result

def is_prime(number):
    number = int(number)
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True