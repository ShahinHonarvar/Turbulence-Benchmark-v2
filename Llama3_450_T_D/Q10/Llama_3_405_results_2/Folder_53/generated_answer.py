def all_odd_ints_exclusive(lst):
    return [num for num in lst[101:100:-1] if num % 2 != 0][::-1]