def all_odd_ints_inclusive(number_list):
    if len(number_list) <= 30:
        return []
    odd_integers = [num for num in number_list[20:31] if num % 2 != 0]
    return odd_integers