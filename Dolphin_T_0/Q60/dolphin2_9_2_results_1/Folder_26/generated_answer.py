def all_left_right_truncatable_prime(x):
    prime = ['2', '3', '5', '7']
    non_prime = []
    left_right_truncatable_prime = []
    for i in range(0, x):
        if i < 10:
            if i not in non_prime:
                prime.append(str(i))
        elif str(i) not in non_prime:
            if is_prime(i):
                if i % 10 != 0:
                    left_right_truncatable_prime.append(str(i))
                else:
                    non_prime.append(str(i))
            else:
                non_prime.append(str(i))
    left_right_truncatable_prime.sort(reverse=True)
    return left_right_truncatable_prime

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True