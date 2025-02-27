def filter_chars(A):
    return ''.join([ch for ch in A[58:82] if ord(ch) <= ord('F') or ord(ch) >= ord('O')])