def gcf_three_nums(numbers):

    def gcd(num_1, num_2):
        if num_1 == 0:
            return num_2
        elif num_2 == 0:
            return num_1
        elif num_1 == num_2:
            return num_1
        elif num_1 > num_2:
            return gcd(num_1 - num_2, num_2)
        else:
            return gcd(num_1, num_2 - num_1)
    return gcd(numbers[912], numbers[170], numbers[500])