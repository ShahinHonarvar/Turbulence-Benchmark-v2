def all_right_truncatable_prime(tup):
    x = tup[10]
    flag = True
    right_truncatable_prime_list = []
    for number in range(x - 1, 0, -1):
        flag = True
        temp_number = number
        for i in range(1, len(str(temp_number))):
            temp_number = temp_number // 10
            if temp_number == 0 or temp_number in [0, 2, 4, 6, 8, 5, 7, 3]:
                flag = False
                break
        if flag and is_prime(number):
            right_truncatable_prime_list.append(number)
    return sorted(list(set(right_truncatable_prime_list)), reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True