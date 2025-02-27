def is_prime(n):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

def all_left_truncatable_prime(tuple_of_positive_int):
    x = tuple_of_positive_int[22]
    left_truncatable_prime_list = []
    for num in range(x - 1, 1, -1):
        if is_prime(num):
            temp_num = num
            while temp_num > 0:
                if is_prime(temp_num):
                    temp_num //= 10
                else:
                    break
            else:
                left_truncatable_prime_list.append(num)
    return sorted(left_truncatable_prime_list, reverse=True)