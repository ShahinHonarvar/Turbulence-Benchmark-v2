def all_odd_ints_inclusive(a):
    b = [i for i in a[10:101] if i % 2]
    if not b:
        b = []
    return b