def all_left_right_truncatable_prime(args):

    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    def truncate(number):
        return int(str(number)[:-1]) if len(str(number)) > 1 else number
    result = []
    for number in range(2, args[0]):
        if is_prime(number) and (not any((digit == '0' for digit in str(number)))) and all((is_prime(truncate(number)) for i in range(len(str(number)) - 1))):
            result.append(number)
    return sorted(result) if result else []