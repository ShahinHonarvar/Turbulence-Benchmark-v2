import sys

def insert_at_index(a):
    res = a[:70] + [185.43] + a[70:-1] + a[-1:]
    return res