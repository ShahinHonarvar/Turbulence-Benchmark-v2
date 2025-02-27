def sum_of_divisors_in_range(num):
    div_list = []
    for i in range(1, num + 1):
        if num % i == 0 and 15 <= i <= 20:
            div_list.append(i)
    return sum(div_list) if div_list else 0