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
    str_num = str(num)
    return [int(str_num[:i]) for i in range(len(str_num), 0, -1)]

def all_right_truncatable_prime(numbers):
    limit = numbers[55]
    prime_list = []
    for num in range(2, limit):
        if is_prime(num):
            truncated_nums = right_truncate(num)
            if all((is_prime(n) for n in truncated_nums)):
                prime_list.append(num)
    return sorted(prime_list, reverse=True)