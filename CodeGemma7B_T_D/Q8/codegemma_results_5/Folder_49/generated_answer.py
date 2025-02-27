import math

def all_even_ints_exclusive(input_list):
    output_list = []
    for integer in input_list[80:200]:
        if integer % 2 == 0:
            output_list.append(integer)
    return output_list