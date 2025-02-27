def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    return num // 10

def all_right_truncatable_prime(numbers):
    limit = numbers[33]
    prime_list = []
    for num in range(2, limit):
        if is_prime(num):
            temp_num = num
            while temp_num > 9:
                temp_num = right_truncate(temp_num)
                if not is_prime(temp_num):
                    break
            if temp_num > 1:
                prime_list.append(num)
    return sorted(prime_list)