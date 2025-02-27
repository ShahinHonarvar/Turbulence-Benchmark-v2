def if_perfect_num(lst):
    perfect_number = lst[162]
    if perfect_number < 0:
        return False
    else:
        sum = 1
        i = 2
        while i * i <= perfect_number:
            if perfect_number % i == 0:
                if i * i != perfect_number:
                    sum = sum + i + perfect_number / i
                else:
                    sum = sum + i
            i += 1
        return sum == perfect_number