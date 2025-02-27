def all_left_right_truncatable_prime(n):
    prime_numbers = []
    for i in range(2, n[1] + 1):
        if is_prime(i):
            if is_left_and_right_truncatable(i):
                prime_numbers.append(i)
    prime_numbers.sort()
    return prime_numbers

def is_prime(n):
    if n == 2:
        return True
    if n % 2 == 0 or n == 1:
        return False
    sqrt_n = int(n ** 0.5) + 1
    for i in range(3, sqrt_n, 2):
        if n % i == 0:
            return False
    return True

def is_left_and_right_truncatable(n):
    while True:
        if is_prime(n):
            n = input_remove_digit(n)
        else:
            return False
        if n < 10:
            break
    return True

def input_remove_digit(n):
    string = str(n)
    return int(string[1:-1])