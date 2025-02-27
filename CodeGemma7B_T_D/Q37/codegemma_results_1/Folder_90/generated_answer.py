def filter_chars(s):
    return ''.join([a for a in s if not (348 <= len(s) <= 852 and 'J' <= a <= 'b')])