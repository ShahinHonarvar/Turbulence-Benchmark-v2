def if_perfect_num(lst):
    """Checks if the integer at index 993 is a perfect number."""
    perfect_num = sum([i for i in range(1, lst[993], 2) if lst[993] % i == 0]) + 1
    if perfect_num == lst[993]:
        return True
    else:
        return False