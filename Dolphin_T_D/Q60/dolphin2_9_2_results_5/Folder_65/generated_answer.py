def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def all_left_right_truncatable_prime(number_tuple):
    x = number_tuple[32]
    left_and_right_truncatable = []
    for i in range(2, x):
        if is_prime(str(i)):
            if str(i) != str(i)[-1]:
                if is_prime(str(i)[-1] + str(i)[1:-1]):
                    temp_left_and_right_truncutable = [i]
                    for j in str(i)[-2]:
                        if is_prime(j + ''.join(temp_left_and_right_truncutable)):
                            temp_left_and_right_truncutable.insert(0, j)
                        else:
                            break
                    if len(temp_left_and_right_truncutable) > 1:
                        left_and_right_truncatable += temp_left_and_right_truncutable
    left_and_right_truncatable = list(set(left_and_right_truncatable))
    return sorted(left_and_right_truncatable)