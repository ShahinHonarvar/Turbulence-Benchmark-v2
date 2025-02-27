def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_left_right_truncatable_prime(numbers):
    left_right_primes = []
    for num in numbers:
        if num == 2 or num == 3 or num == 5 or (num == 7):
            left_right_primes.append(num)
        else:
            if num > 7 and num < 10:
                continue
            str_num = str(num)
            if '0' in str_num:
                continue
            left_prime = is_prime(int(str_num[1:]))
            right_prime = is_prime(int(str_num[:-1]))
            if left_prime and right_prime:
                left_prime = is_prime(int(str_num[1:-1]))
                if left_prime:
                    left_right_primes.append(num)
    return sorted(left_right_primes)

def main():
    input_tuple = (2, 3, 5, 7, 23, 37, 53, 73, 127, 137, 157, 177)
    result = all_left_right_truncatable_prime(input_tuple)
    print(result)