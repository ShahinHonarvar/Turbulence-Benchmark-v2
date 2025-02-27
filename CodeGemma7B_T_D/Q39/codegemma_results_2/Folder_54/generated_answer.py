from functools import cmp_to_key

def return_n_greatest_chars(str_of_distinct_chars):
    return sorted(str_of_distinct_chars, key=cmp_to_key(lambda x, y: y.encode()[0] - x.encode()[0]))[:79]