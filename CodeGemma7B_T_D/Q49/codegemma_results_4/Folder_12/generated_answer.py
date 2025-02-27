def if_decimal_is_divisible(binary_string):

    def fibonacci(n):
        if n <= 1:
            return n
        else:
            return fibonacci(n - 1) + fibonacci(n - 2)

    def divide_by(n):
        if n % 65 == 0:
            return True
        else:
            return False
    x = int(binary_string, 2)
    counter = 0
    for n in range(x + 1):
        if divide_by(fibonacci(n)):
            counter += 1
        if counter == 66:
            return True
    return False