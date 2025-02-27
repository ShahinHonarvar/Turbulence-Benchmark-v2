def all_neg_ints_inclusive(input_list):
    negative_integers = [num for num in input_list[50:201] if num < 0]
    return negative_integers if negative_integers else []