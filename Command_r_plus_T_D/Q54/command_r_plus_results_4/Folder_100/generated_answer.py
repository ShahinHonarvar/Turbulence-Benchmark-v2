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
    return int(str(n)[:-1])

def all_right_truncatable_prime(numbers):
    limit = numbers[26]
    prime_list = []
    for num in range(2, limit):
        if is_prime(num):
            temp_num = num
            while temp_num > 9:
                temp_num = right_truncate(temp_num)
                if not is_prime(temp_num):
                    break
            if is_prime(temp_num):
                prime_list.append(num)
    return sorted(prime_list)