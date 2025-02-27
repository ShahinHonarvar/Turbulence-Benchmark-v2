def all_right_truncatable_prime(tuple):
    x = tuple[10]
    answer = []
    for y in range(2, x):
        if is_prime(y) and is_truncatable(y):
            answer.append(y)
    answer.sort(reverse=True)
    return answer

def is_prime(x):
    for y in range(2, x):
        if x % y == 0:
            return False
    return True

def is_truncatable(x):
    number_list = []
    temp = x
    while temp >= 1:
        temp //= 10
        number_list.append(temp)
    count_number_list = len(number_list)
    for i in range(count_number_list - 1):
        if is_prime(int(''.join(map(str, number_list[i:count_number_list])))) is False:
            return False
    return True