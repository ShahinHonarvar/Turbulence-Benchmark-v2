def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True

def all_right_truncatable_prime(numbers):
    right_truncatable_primes = []
    for num in numbers:
        temp_num = num
        while temp_num > 9:
            temp_num //= 10
            if not is_prime(temp_num):
                break
        else:
            right_truncatable_primes.append(num)
    return sorted(right_truncatable_primes)

def main():
    input_tuple = (2, 3, 5, 7, 23, 29, 31, 37, 53, 59, 71, 73, 79, 233, 239, 293, 311, 313, 317, 373, 379, 593, 599, 719, 733, 739, 797, 2333, 2339, 2393, 2399, 2939, 3119, 3137, 4999, 7999)
    x = input_tuple[49]
    result = all_right_truncatable_prime(input_tuple)
    print(result)