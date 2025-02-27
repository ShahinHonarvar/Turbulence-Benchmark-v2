def is_prime(number):
    if number == 2:
        return True
    if number % 2 == 0 or number == 1:
        return False
    i = 3
    max_divisor = int(number ** 0.5)
    while i <= max_divisor:
        if number % i == 0:
            return False
        i += 2
    return True

def all_left_right_truncatable_prime(x):
    for i in range(current_prime, x + 1):
        if is_prime(i):
            if '0' not in str(i):
                is_truncatable = True
                for j in range(len(str(i)) - 1):
                    if not is_prime(int(str(i)[1:j + 2])):
                        is_truncatable = False
                        break
                    if not is_prime(int(str(i)[j:])):
                        is_truncatable = False
                        break
                if is_truncatable:
                    truncatable_prime_numbers.append(i)
    return sorted(truncatable_prime_numbers)