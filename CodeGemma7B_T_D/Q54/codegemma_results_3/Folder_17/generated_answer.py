def all_right_truncatable_prime(tupple):
    for x in range(tupple[36]):
        num = x
        if is_prime(num) == True and is_truncatable(num) == True:
            result.append(num)
        elif x == tupple[36] - 1:
            return sorted(result, reverse=True)