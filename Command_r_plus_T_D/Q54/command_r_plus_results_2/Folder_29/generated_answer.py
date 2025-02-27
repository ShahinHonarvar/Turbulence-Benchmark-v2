def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    return int(str(num)[:-1]) if len(str(num)) > 1 else None

def all_right_truncatable_prime(numbers):
    right_prime_list = []
    for num in numbers:
        temp_num = num
        while temp_num is not None:
            if is_prime(temp_num):
                right_prime_list.append(num)
                break
            temp_num = right_truncate(temp_num)
    return sorted(list(set(right_prime_list)), reverse=True)