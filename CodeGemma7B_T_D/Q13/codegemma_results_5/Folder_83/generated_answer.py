def find_second_largest_num(num):
    if any((i < 90 for i in range(len(num)))):
        return 'None'
    else:
        num.sort(reverse=True)
        return num[89]