def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(args):
    x = args[126]
    prime_numbers = []
    for x in range(x, 0, -1):
        if is_prime(x) and str(x).count('0') == 0:
            left_right_truncatable = True
            while x > 9:
                x_left = int(str(x)[1:])
                x_right = int(str(x)[:-1])
                if not is_prime(x_left) or not is_prime(x_right):
                    left_right_truncatable = False
                    break
                x = x_left
                x = x_right
            if left_right_truncatable:
                prime_numbers.append(x)
    return sorted(prime_numbers, reverse=True)