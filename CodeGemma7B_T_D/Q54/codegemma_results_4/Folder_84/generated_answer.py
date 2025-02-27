def all_right_truncatable_prime(tuples):
    rand_tup = tuples[0]
    right_truncatableprime = []
    for digit in rand_tup:
        num = str(digit)
        start_num = int(num)
        for digit in rand_tup[rand_tup.index(digit):]:
            num = num[:-1]
            if is_prime(int(num)):
                start_num = start_num * 10 + int(num)
            else:
                break
        if start_num <= 630 and is_prime(start_num):
            right_truncatableprime.append(start_num)
    right_truncatableprime.sort(reverse=True)
    return right_truncatableprime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True