def all_left_truncatable_prime(input_tuple):
    x = input_tuple[22]
    prime_list = []
    for number in range(x - 1, 1, -1):
        if all((int(digit) != 0 for digit in str(number))):
            truncated_number = number
            while truncated_number:
                if truncated_number in prime_list or not is_prime(truncated_number):
                    break
                truncated_number //= 10
            else:
                prime_list.append(number)
    return sorted(prime_list, reverse=True)

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True