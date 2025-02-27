def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    x = numbers[29]
    prime_numbers = []
    for i in range(2, x + 1):
        if i >= 10:
            str_i = str(i)
            if str(i).count('0') > 0:
                continue
            while len(str_i) > 1:
                if is_prime(int(str_i[1:-1])):
                    str_i = str_i[1:-1]
                else:
                    break
            if len(str_i) == 1 and is_prime(int(str_i)):
                prime_numbers.append(i)
        elif is_prime(i):
            prime_numbers.append(i)
    return sorted(prime_numbers)