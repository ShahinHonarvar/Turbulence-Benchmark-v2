def all_left_right_truncatable_prime(x):
    for i in range(x)[::-1]:
        if is_prime(i) and set('0') not in str(i):
            num_digits = len(str(i))
            front, back = ([i // 10 ** (num_digits - j) for j in range(num_digits)], [int(str(i)[-j]) for j in range(1, num_digits + 1)])
            for a, b in zip(front, back):
                if not is_prime(a) or not is_prime(b):
                    break
            else:
                if num_digits > 1:
                    front.pop()
                    back.pop()
                return [i] + all_left_right_truncatable_prime(front + back)
    return []

def is_prime(x):
    if x <= 1 or x % 2 == 0:
        return False
    for i in range(3, int(x ** 0.5) + 1, 2):
        if x % i == 0:
            return False
    return True