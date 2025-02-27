def all_right_truncatable_prime(tuple_list):
    prime_list = []
    for number in tuple_list:
        if is_prime(number):
            for i in range(1, len(str(number))):
                if not is_prime(int(str(number)[:-i])):
                    break
            else:
                prime_list.append(number)
    prime_list.sort(reverse=True)
    return prime_list

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True