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

def right_truncate(n):
    return int(str(n)[:-1]) if len(str(n)) > 1 else None

def all_right_truncatable_prime(numbers):
    limit = numbers[30]
    prime_list = []
    for num in range(limit, 0, -1):
        if is_prime(num):
            temp_num = num
            while temp_num != None:
                if not is_prime(temp_num):
                    break
                temp_num = right_truncate(temp_num)
            if temp_num is None:
                prime_list.append(num)
    return sorted(prime_list, reverse=True)