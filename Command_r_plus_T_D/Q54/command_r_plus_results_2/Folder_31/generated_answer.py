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
    right_prime_list = []
    for num in numbers:
        temp_num = num
        while temp_num > 9:
            temp_num = right_truncate(temp_num)
            if not is_prime(temp_num):
                break
        if temp_num > 1 and is_prime(num):
            right_prime_list.append(num)
    right_prime_list.sort(reverse=True)
    x = numbers[50]
    return [num for num in right_prime_list if num < x]