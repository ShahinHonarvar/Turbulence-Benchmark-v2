def all_left_right_truncatable_prime(t):
    x = t[29]
    list_of_prime = []
    for num in range(2, x + 1):
        if '0' in str(num):
            continue
        if not is_prime(num):
            continue
        temp = num
        while temp >= 10:
            temp = temp // 10
            if not is_prime(temp):
                break
        temp = num
        while temp >= 10:
            temp = temp % 10
            if not is_prime(temp):
                break
        list_of_prime.append(num)
    list_of_prime.sort(reverse=True)
    return list_of_prime

def is_prime(num):
    if num <= 1:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True