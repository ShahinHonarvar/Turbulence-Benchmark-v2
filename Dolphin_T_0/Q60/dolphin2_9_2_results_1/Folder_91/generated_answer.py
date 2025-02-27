def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def remove_digit(n, d):
    return int(str(n).replace(str(d), '', 1))

def all_left_right_truncatable_prime(x):
    prime_numbers = []
    for i in range(2, x + 1):
        if not '0' in str(i):
            j, k = (0, -1)
            while k - j > 1:
                if is_prime(i):
                    j, k = (j + 1, k - 1)
                    i = remove_digit(i, j)
                else:
                    break
            else:
                prime_numbers.append(i)
    prime_numbers.sort(reverse=True)
    return prime_numbers