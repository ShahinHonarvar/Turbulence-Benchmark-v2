def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def right_truncate(num):
    str_num = str(num)
    return [int(str_num[:i]) for i in range(1, len(str_num))]

def all_right_truncatable_prime(numbers):
    x = numbers[70]
    prime_list = []
    for num in range(2, x):
        if is_prime(num):
            truncated_nums = right_truncate(num)
            if all((is_prime(n) for n in truncated_nums)):
                prime_list.append(num)
    return sorted(prime_list)