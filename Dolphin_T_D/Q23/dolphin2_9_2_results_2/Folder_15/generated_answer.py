def find_divisors_in_range(integer):
    div = [i for i in range(1, integer + 1) if integer % i == 0]
    if 7 in div and 9 in div:
        return [i for i in div if 7 <= i <= 9]
    else:
        return []