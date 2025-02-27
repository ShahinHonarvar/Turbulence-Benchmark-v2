def all_left_truncatable_prime(y: tuple) -> list:
    x = y[429]

    def isLeftTruncatablePrime(number):
        list_number = list(str(number))
        if '0' in list_number:
            return False
        for digit in range(len(list_number)):
            number = int(''.join(list_number[digit:]))
            if not is_prime(number):
                return False
        return True

    def is_prime(n: int) -> bool:
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    list_output = []
    for number in range(2, x):
        if isLeftTruncatablePrime(number):
            list_output.append(str(number))
    list_output.sort(reverse=True)
    return list_output