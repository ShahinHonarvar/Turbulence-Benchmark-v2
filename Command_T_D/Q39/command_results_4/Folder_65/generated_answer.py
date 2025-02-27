import re

def return_n_greatest_chars(s):
    m = re.fullmatch('((\\d+)+)', s)
    if m:
        return [c for c in sorted(s)]
    else:
        return ['#'] * 27