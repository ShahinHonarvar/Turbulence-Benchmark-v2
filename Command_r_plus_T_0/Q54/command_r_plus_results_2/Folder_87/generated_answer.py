def is_prime(num):
    if num <= 1:
        return False
    if num <= 3:
        return True
    if num % 2 == 0 or num % 3 == 0:
        return False
    i = 5
    while i * i <= num:
        if num % i == 0 or num % (i + 2) == 0:
            return False
        i += 6
    return True

def right_truncate(num):
    return int(str(num)[:-1]) if len(str(num)) > 1 else None

def all_right_truncatable_prime(numbers):
    limit = numbers[39]
    prime_list = []
    for num in range(limit, 0, -1):
        if is_prime(num):
            temp_num = num
            while temp_num is not None:
                if not is_prime(temp_num):
                    break
                temp_num = right_truncate(temp_num)
            if temp_num is None:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)