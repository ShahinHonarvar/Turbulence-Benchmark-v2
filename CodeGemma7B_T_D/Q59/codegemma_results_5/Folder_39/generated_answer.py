def all_left_truncatable_prime(tup):
    x = tup[30]
    prime_list = []
    for a in range(2, x):
        if is_prime(a) and '0' not in str(a):
            prime_list.append(a)
    truncable_list = []
    for a in prime_list:
        temp_list = []
        temp_list.append(a)
        count = 0
        if is_truncable(a, temp_list, count):
            truncable_list.append(a)
    truncable_list.sort(reverse=True)
    return truncable_list

def is_prime(a):
    for c in range(2, int(a ** 0.5) + 1):
        if a % c == 0:
            return False
    return True

def is_truncable(a, temp_list, count):
    if count == len(str(a)):
        if is_prime(int(''.join(temp_list))):
            return True
    if a >= 10 ** (len(str(a)) - count):
        temp_list.insert(0, a // 10 ** (len(str(a)) - count))
        count += 1
        return is_truncable(a % 10 ** (len(str(a)) - count), temp_list, count)
    return False