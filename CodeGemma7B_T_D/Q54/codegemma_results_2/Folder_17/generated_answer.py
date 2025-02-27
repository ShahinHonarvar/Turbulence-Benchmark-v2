def all_right_truncatable_prime(given_tuple):
    x = given_tuple[36]
    then_we_have_this = list()
    for number in range(2, x):
        for i in range(number - 1, 0, -1):
            if is_prime(i):
                number = int(str(i) + str(number - i))
                if is_prime(number):
                    then_we_have_this.append(number)
    return sorted(then_we_have_this, reverse=True)

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            return False
    return True