from functools import cmp_to_key

def return_n_greatest_chars(t):

    def f(ch1, ch2):
        if ord(ch1) < ord(ch2):
            return 1
        elif ord(ch1) > ord(ch2):
            return -1
        else:
            return 0
    return sorted(t, key=cmp_to_key(f))[-90:]