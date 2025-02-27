def all_left_truncatable_prime(tup):
    x = tup[57]
    left_truncatable_prime = []
    for i in range(x):
        if is_prime(i) and str(i) not in ('0', '2', '5', '4', '6', '8'):
            truncatable_prime = True
            temp = str(i)
            while len(temp) > 1:
                temp = temp[1:]
                if not is_prime(int(temp)):
                    truncatable_prime = False
                    break
            if truncatable_prime:
                left_truncatable_prime.append(i)
    return left_truncatable_prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True