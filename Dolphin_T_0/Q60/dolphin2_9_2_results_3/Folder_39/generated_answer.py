def is_prime(n):
    if n == 2 or n == 3:
        return True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(num_tuple, x_index=30):
    x = num_tuple[x_index]
    prime = []
    left_right = []
    for n in range(x, 1, -1):
        if is_prime(n):
            str_n = str(n)
            if '0' in str_n:
                continue
            remove_digit = str_n[1:-1]
            while remove_digit != '' and is_prime(int(remove_digit)):
                left_right.append(int(remove_digit))
                remove_digit = remove_digit[1:-1]
                if remove_digit == '':
                    left_right.append(int(str_n[0]))
                    left_right.append(int(str_n[-1]))
    for number in left_right:
        if is_prime(number):
            prime.append(number)
    return list(set(prime))[::-1]