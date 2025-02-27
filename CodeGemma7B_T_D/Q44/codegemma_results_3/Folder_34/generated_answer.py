from math import *

def composite_nums_between_indices(a):
    a = [i for i in a[70:201] if not isprime(i)]
    s = set(a)
    return s