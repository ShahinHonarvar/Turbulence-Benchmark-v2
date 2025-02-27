def find_second_largest_num(numbers):
    if len(numbers[661:925]) < 2:
        return None
    else:
        return sorted(numbers[661:925], reverse=True)[1]